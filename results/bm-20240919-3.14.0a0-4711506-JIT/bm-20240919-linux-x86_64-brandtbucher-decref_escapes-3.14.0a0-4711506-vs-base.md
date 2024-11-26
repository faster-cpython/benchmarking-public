# Results vs. base

- fork: brandtbucher
- ref: decref_escapes
- machine: linux-x86_64
- commit hash: 4711506
- commit date: 2024-09-19
- overall geometric mean: 1.002x slower
- HPT reliability: 97.61%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                              | 2.97 sec: 1.01x slower                                                |
| html5lib       | 64.5 ms                                                               | 63.8 ms: 1.01x faster                                                 |
| tornado_http   | 94.6 ms                                                               | 95.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_generators | 461 ms                                                                | 451 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl  | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                                |
| coroutines       | 22.9 ms                                                               | 23.0 ms: 1.01x slower                                                 |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_tcp, asyncio_websockets, async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 70.0 ms                                                               | 70.7 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.80 ms                                                               | 3.68 ms: 1.03x faster                                                 |
| regex_compile  | 141 ms                                                                | 142 ms: 1.00x slower                                                  |
| regex_v8       | 24.7 ms                                                               | 25.1 ms: 1.02x slower                                                 |
| regex_dna      | 216 ms                                                                | 224 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process  | 55.6 ms                                                               | 54.6 ms: 1.02x faster                                                 |
| xml_etree_generate | 78.7 ms                                                               | 77.9 ms: 1.01x faster                                                 |
| tomli_loads        | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                |
| json_dumps         | 10.1 ms                                                               | 10.3 ms: 1.02x slower                                                 |
| pickle_dict        | 34.5 us                                                               | 35.2 us: 1.02x slower                                                 |
| json_loads         | 26.7 us                                                               | 27.5 us: 1.03x slower                                                 |
| pickle_list        | 5.17 us                                                               | 5.37 us: 1.04x slower                                                 |
| unpickle           | 14.6 us                                                               | 15.3 us: 1.05x slower                                                 |
| Geometric mean     | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (6): pickle, pickle_pure_python, unpickle_list, unpickle_pure_python, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                 |
| python_startup_no_site | 7.07 ms                                                               | 7.08 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text    | 25.4 ms                                                               | 24.5 ms: 1.04x faster                                                 |
| genshi_xml     | 60.0 ms                                                               | 58.0 ms: 1.04x faster                                                 |
| mako           | 9.88 ms                                                               | 9.97 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpack_sequence          | 112 ns                                                                | 106 ns: 1.06x faster                                                  |
| typing_runtime_protocols | 166 us                                                                | 160 us: 1.04x faster                                                  |
| genshi_text              | 25.4 ms                                                               | 24.5 ms: 1.04x faster                                                 |
| genshi_xml               | 60.0 ms                                                               | 58.0 ms: 1.04x faster                                                 |
| regex_effbot             | 3.80 ms                                                               | 3.68 ms: 1.03x faster                                                 |
| gc_traversal             | 3.94 ms                                                               | 3.83 ms: 1.03x faster                                                 |
| pprint_pformat           | 1.60 sec                                                              | 1.56 sec: 1.02x faster                                                |
| async_generators         | 461 ms                                                                | 451 ms: 1.02x faster                                                  |
| xml_etree_process        | 55.6 ms                                                               | 54.6 ms: 1.02x faster                                                 |
| logging_simple           | 5.75 us                                                               | 5.65 us: 1.02x faster                                                 |
| logging_format           | 6.24 us                                                               | 6.13 us: 1.02x faster                                                 |
| telco                    | 8.05 ms                                                               | 7.94 ms: 1.01x faster                                                 |
| deepcopy_memo            | 27.2 us                                                               | 26.9 us: 1.01x faster                                                 |
| html5lib                 | 64.5 ms                                                               | 63.8 ms: 1.01x faster                                                 |
| xml_etree_generate       | 78.7 ms                                                               | 77.9 ms: 1.01x faster                                                 |
| deepcopy_reduce          | 2.68 us                                                               | 2.66 us: 1.01x faster                                                 |
| coverage                 | 85.2 ms                                                               | 84.5 ms: 1.01x faster                                                 |
| sqlglot_parse            | 1.35 ms                                                               | 1.34 ms: 1.01x faster                                                 |
| sqlglot_transpile        | 1.69 ms                                                               | 1.69 ms: 1.01x faster                                                 |
| logging_silent           | 104 ns                                                                | 103 ns: 1.01x faster                                                  |
| sympy_expand             | 506 ms                                                                | 504 ms: 1.00x faster                                                  |
| sqlglot_optimize         | 58.2 ms                                                               | 57.9 ms: 1.00x faster                                                 |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                 |
| python_startup_no_site   | 7.07 ms                                                               | 7.08 ms: 1.00x slower                                                 |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                                |
| regex_compile            | 141 ms                                                                | 142 ms: 1.00x slower                                                  |
| docutils                 | 2.96 sec                                                              | 2.97 sec: 1.01x slower                                                |
| bpe_tokeniser            | 4.44 sec                                                              | 4.47 sec: 1.01x slower                                                |
| meteor_contest           | 107 ms                                                                | 107 ms: 1.01x slower                                                  |
| tornado_http             | 94.6 ms                                                               | 95.1 ms: 1.01x slower                                                 |
| pyflate                  | 448 ms                                                                | 451 ms: 1.01x slower                                                  |
| go                       | 131 ms                                                                | 132 ms: 1.01x slower                                                  |
| scimark_fft              | 308 ms                                                                | 310 ms: 1.01x slower                                                  |
| sqlite_synth             | 2.74 us                                                               | 2.76 us: 1.01x slower                                                 |
| comprehensions           | 16.6 us                                                               | 16.8 us: 1.01x slower                                                 |
| dulwich_log              | 67.8 ms                                                               | 68.3 ms: 1.01x slower                                                 |
| coroutines               | 22.9 ms                                                               | 23.0 ms: 1.01x slower                                                 |
| generators               | 32.8 ms                                                               | 33.1 ms: 1.01x slower                                                 |
| mako                     | 9.88 ms                                                               | 9.97 ms: 1.01x slower                                                 |
| create_gc_cycles         | 1.74 ms                                                               | 1.75 ms: 1.01x slower                                                 |
| tomli_loads              | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                |
| float                    | 70.0 ms                                                               | 70.7 ms: 1.01x slower                                                 |
| regex_v8                 | 24.7 ms                                                               | 25.1 ms: 1.02x slower                                                 |
| mdp                      | 2.66 sec                                                              | 2.70 sec: 1.02x slower                                                |
| json_dumps               | 10.1 ms                                                               | 10.3 ms: 1.02x slower                                                 |
| hexiom                   | 6.86 ms                                                               | 6.98 ms: 1.02x slower                                                 |
| pprint_safe_repr         | 748 ms                                                                | 761 ms: 1.02x slower                                                  |
| deepcopy                 | 258 us                                                                | 263 us: 1.02x slower                                                  |
| scimark_sparse_mat_mult  | 4.21 ms                                                               | 4.29 ms: 1.02x slower                                                 |
| pickle_dict              | 34.5 us                                                               | 35.2 us: 1.02x slower                                                 |
| crypto_pyaes             | 65.8 ms                                                               | 67.2 ms: 1.02x slower                                                 |
| nqueens                  | 85.5 ms                                                               | 87.9 ms: 1.03x slower                                                 |
| spectral_norm            | 98.4 ms                                                               | 102 ms: 1.03x slower                                                  |
| json_loads               | 26.7 us                                                               | 27.5 us: 1.03x slower                                                 |
| pickle_list              | 5.17 us                                                               | 5.37 us: 1.04x slower                                                 |
| regex_dna                | 216 ms                                                                | 224 ms: 1.04x slower                                                  |
| json                     | 4.94 ms                                                               | 5.14 ms: 1.04x slower                                                 |
| chaos                    | 58.0 ms                                                               | 60.8 ms: 1.05x slower                                                 |
| pycparser                | 1.15 sec                                                              | 1.21 sec: 1.05x slower                                                |
| unpickle                 | 14.6 us                                                               | 15.3 us: 1.05x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (37): async_tree_cpu_io_mixed, async_tree_none, scimark_monte_carlo, pylint, sympy_sum, raytrace, sqlglot_normalize, scimark_sor, scimark_lu, pickle, bench_thread_pool, sympy_str, pickle_pure_python, async_tree_cpu_io_mixed_tg, unpickle_list, deltablue, bench_mp_pool, pathlib, nbody, asyncio_tcp, pidigits, richards_super, sympy_integrate, richards, unpickle_pure_python, asyncio_websockets, 2to3, django_template, xml_etree_iterparse, async_tree_io, fannkuch, async_tree_memoization_tg, async_tree_none_tg, thrift, async_tree_memoization, xml_etree_parse, async_tree_io_tg

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 97.61% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x