
# Results vs. base

- fork: iritkatriel
- ref: InitializeHeader
- machine: linux-x86_64
- commit hash: e73d0cf
- commit date: 2023-01-04
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230103-linux-x86_64-python-64ed609c532a12b27f67-3.12.0a3+-64ed609 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 252 ms: 1.00x faster                                                    |
| chameleon      | 6.34 ms                                                                | 6.17 ms: 1.03x faster                                                   |
| docutils       | 2.49 sec                                                               | 2.51 sec: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230103-linux-x86_64-python-64ed609c532a12b27f67-3.12.0a3+-64ed609 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 93.7 ms                                                                | 92.8 ms: 1.01x faster                                                   |
| pidigits       | 198 ms                                                                 | 192 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230103-linux-x86_64-python-64ed609c532a12b27f67-3.12.0a3+-64ed609 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 131 ms: 1.02x slower                                                    |
| regex_dna      | 215 ms                                                                 | 211 ms: 1.02x faster                                                    |
| regex_effbot   | 3.70 ms                                                                | 3.58 ms: 1.03x faster                                                   |
| regex_v8       | 22.2 ms                                                                | 22.5 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230103-linux-x86_64-python-64ed609c532a12b27f67-3.12.0a3+-64ed609 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 9.52 ms                                                                | 9.42 ms: 1.01x faster                                                   |
| json_loads           | 23.9 us                                                                | 24.0 us: 1.01x slower                                                   |
| pickle               | 10.1 us                                                                | 10.2 us: 1.01x slower                                                   |
| pickle_dict          | 31.1 us                                                                | 30.4 us: 1.02x faster                                                   |
| pickle_list          | 4.07 us                                                                | 4.11 us: 1.01x slower                                                   |
| unpickle_list        | 5.23 us                                                                | 4.94 us: 1.06x faster                                                   |
| unpickle_pure_python | 198 us                                                                 | 196 us: 1.01x faster                                                    |
| xml_etree_generate   | 76.1 ms                                                                | 75.7 ms: 1.01x faster                                                   |
| xml_etree_process    | 53.4 ms                                                                | 53.7 ms: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (4): pickle_pure_python, unpickle, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230103-linux-x86_64-python-64ed609c532a12b27f67-3.12.0a3+-64ed609 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 8.45 ms                                                                | 8.48 ms: 1.00x slower                                                   |
| python_startup_no_site | 6.05 ms                                                                | 6.08 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230103-linux-x86_64-python-64ed609c532a12b27f67-3.12.0a3+-64ed609 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 20.2 ms                                                                | 20.4 ms: 1.01x slower                                                   |
| genshi_xml     | 47.2 ms                                                                | 46.3 ms: 1.02x faster                                                   |
| mako           | 9.60 ms                                                                | 9.83 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20230103-linux-x86_64-python-64ed609c532a12b27f67-3.12.0a3+-64ed609 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3                    | 253 ms                                                                 | 252 ms: 1.00x faster                                                    |
| async_generators        | 354 ms                                                                 | 355 ms: 1.00x slower                                                    |
| async_tree_memoization  | 639 ms                                                                 | 623 ms: 1.02x faster                                                    |
| chameleon               | 6.34 ms                                                                | 6.17 ms: 1.03x faster                                                   |
| chaos                   | 66.5 ms                                                                | 67.9 ms: 1.02x slower                                                   |
| bench_thread_pool       | 778 us                                                                 | 774 us: 1.00x faster                                                    |
| crypto_pyaes            | 73.7 ms                                                                | 73.5 ms: 1.00x faster                                                   |
| deepcopy                | 334 us                                                                 | 330 us: 1.01x faster                                                    |
| deepcopy_reduce         | 2.93 us                                                                | 2.90 us: 1.01x faster                                                   |
| deepcopy_memo           | 34.3 us                                                                | 33.7 us: 1.02x faster                                                   |
| deltablue               | 3.22 ms                                                                | 3.34 ms: 1.04x slower                                                   |
| docutils                | 2.49 sec                                                               | 2.51 sec: 1.01x slower                                                  |
| dulwich_log             | 62.3 ms                                                                | 62.0 ms: 1.00x faster                                                   |
| fannkuch                | 366 ms                                                                 | 368 ms: 1.01x slower                                                    |
| generators              | 76.4 ms                                                                | 77.1 ms: 1.01x slower                                                   |
| genshi_text             | 20.2 ms                                                                | 20.4 ms: 1.01x slower                                                   |
| genshi_xml              | 47.2 ms                                                                | 46.3 ms: 1.02x faster                                                   |
| go                      | 133 ms                                                                 | 135 ms: 1.02x slower                                                    |
| json_dumps              | 9.52 ms                                                                | 9.42 ms: 1.01x faster                                                   |
| json_loads              | 23.9 us                                                                | 24.0 us: 1.01x slower                                                   |
| logging_format          | 6.31 us                                                                | 6.35 us: 1.01x slower                                                   |
| logging_silent          | 91.1 ns                                                                | 90.4 ns: 1.01x faster                                                   |
| logging_simple          | 5.68 us                                                                | 5.76 us: 1.01x slower                                                   |
| mako                    | 9.60 ms                                                                | 9.83 ms: 1.02x slower                                                   |
| mdp                     | 2.49 sec                                                               | 2.57 sec: 1.03x slower                                                  |
| nbody                   | 93.7 ms                                                                | 92.8 ms: 1.01x faster                                                   |
| nqueens                 | 79.1 ms                                                                | 80.6 ms: 1.02x slower                                                   |
| pickle                  | 10.1 us                                                                | 10.2 us: 1.01x slower                                                   |
| pickle_dict             | 31.1 us                                                                | 30.4 us: 1.02x faster                                                   |
| pickle_list             | 4.07 us                                                                | 4.11 us: 1.01x slower                                                   |
| pidigits                | 198 ms                                                                 | 192 ms: 1.03x faster                                                    |
| pprint_pformat          | 1.39 sec                                                               | 1.38 sec: 1.01x faster                                                  |
| pyflate                 | 406 ms                                                                 | 391 ms: 1.04x faster                                                    |
| python_startup          | 8.45 ms                                                                | 8.48 ms: 1.00x slower                                                   |
| python_startup_no_site  | 6.05 ms                                                                | 6.08 ms: 1.00x slower                                                   |
| raytrace                | 279 ms                                                                 | 282 ms: 1.01x slower                                                    |
| regex_compile           | 129 ms                                                                 | 131 ms: 1.02x slower                                                    |
| regex_dna               | 215 ms                                                                 | 211 ms: 1.02x faster                                                    |
| regex_effbot            | 3.70 ms                                                                | 3.58 ms: 1.03x faster                                                   |
| regex_v8                | 22.2 ms                                                                | 22.5 ms: 1.01x slower                                                   |
| richards                | 41.3 ms                                                                | 42.4 ms: 1.03x slower                                                   |
| scimark_lu              | 108 ms                                                                 | 107 ms: 1.01x faster                                                    |
| scimark_sparse_mat_mult | 4.20 ms                                                                | 4.10 ms: 1.02x faster                                                   |
| spectral_norm           | 95.1 ms                                                                | 97.5 ms: 1.03x slower                                                   |
| sqlglot_parse           | 1.38 ms                                                                | 1.41 ms: 1.02x slower                                                   |
| sqlglot_transpile       | 1.68 ms                                                                | 1.71 ms: 1.02x slower                                                   |
| sqlglot_optimize        | 51.3 ms                                                                | 50.8 ms: 1.01x faster                                                   |
| sqlglot_normalize       | 106 ms                                                                 | 105 ms: 1.01x faster                                                    |
| sympy_integrate         | 20.4 ms                                                                | 20.4 ms: 1.00x faster                                                   |
| telco                   | 6.33 ms                                                                | 6.41 ms: 1.01x slower                                                   |
| unpickle_list           | 5.23 us                                                                | 4.94 us: 1.06x faster                                                   |
| unpickle_pure_python    | 198 us                                                                 | 196 us: 1.01x faster                                                    |
| xml_etree_generate      | 76.1 ms                                                                | 75.7 ms: 1.01x faster                                                   |
| xml_etree_process       | 53.4 ms                                                                | 53.7 ms: 1.01x slower                                                   |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (30): async_tree_none, async_tree_cpu_io_mixed, async_tree_io, bench_mp_pool, coroutines, coverage, django_template, djangocms, float, hexiom, html5lib, json, meteor_contest, mypy, pathlib, pickle_pure_python, pprint_safe_repr, pycparser, scimark_fft, scimark_monte_carlo, scimark_sor, sqlite_synth, sympy_expand, sympy_sum, sympy_str, thrift, unpack_sequence, unpickle, xml_etree_parse, xml_etree_iterparse
