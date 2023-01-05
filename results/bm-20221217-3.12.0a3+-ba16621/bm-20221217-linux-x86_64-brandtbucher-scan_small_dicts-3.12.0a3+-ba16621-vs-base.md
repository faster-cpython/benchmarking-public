
# Results vs. base

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: ba16621
- commit date: 2022-12-17
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| chameleon      | 6.32 ms                                                                | 6.26 ms: 1.01x faster                                                    |
| docutils       | 2.49 sec                                                               | 2.51 sec: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 192 ms                                                                 | 198 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 208 ms                                                                 | 208 ms: 1.00x faster                                                     |
| regex_v8       | 22.4 ms                                                                | 21.3 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 9.28 ms                                                                | 9.39 ms: 1.01x slower                                                    |
| json_loads           | 23.5 us                                                                | 24.0 us: 1.02x slower                                                    |
| pickle               | 10.00 us                                                               | 10.1 us: 1.01x slower                                                    |
| pickle_dict          | 30.6 us                                                                | 30.9 us: 1.01x slower                                                    |
| pickle_list          | 3.97 us                                                                | 4.10 us: 1.03x slower                                                    |
| pickle_pure_python   | 283 us                                                                 | 281 us: 1.00x faster                                                     |
| unpickle_list        | 5.03 us                                                                | 5.09 us: 1.01x slower                                                    |
| unpickle_pure_python | 199 us                                                                 | 197 us: 1.01x faster                                                     |
| xml_etree_parse      | 150 ms                                                                 | 148 ms: 1.02x faster                                                     |
| xml_etree_generate   | 76.5 ms                                                                | 76.2 ms: 1.00x faster                                                    |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (3): unpickle, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.45 ms                                                                | 8.51 ms: 1.01x slower                                                    |
| python_startup_no_site | 6.06 ms                                                                | 6.09 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 32.4 ms                                                                | 32.2 ms: 1.01x faster                                                    |
| genshi_text     | 20.6 ms                                                                | 20.3 ms: 1.01x faster                                                    |
| genshi_xml      | 47.6 ms                                                                | 46.9 ms: 1.02x faster                                                    |
| mako            | 9.63 ms                                                                | 9.42 ms: 1.02x faster                                                    |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_generators        | 354 ms                                                                 | 348 ms: 1.02x faster                                                     |
| async_tree_io           | 1.33 sec                                                               | 1.31 sec: 1.01x faster                                                   |
| async_tree_memoization  | 650 ms                                                                 | 629 ms: 1.03x faster                                                     |
| chameleon               | 6.32 ms                                                                | 6.26 ms: 1.01x faster                                                    |
| chaos                   | 69.0 ms                                                                | 67.3 ms: 1.02x faster                                                    |
| coroutines              | 25.8 ms                                                                | 25.3 ms: 1.02x faster                                                    |
| coverage                | 98.7 ms                                                                | 101 ms: 1.02x slower                                                     |
| crypto_pyaes            | 74.4 ms                                                                | 75.5 ms: 1.01x slower                                                    |
| deepcopy                | 334 us                                                                 | 323 us: 1.03x faster                                                     |
| deepcopy_reduce         | 2.95 us                                                                | 2.90 us: 1.02x faster                                                    |
| deepcopy_memo           | 33.9 us                                                                | 33.2 us: 1.02x faster                                                    |
| django_template         | 32.4 ms                                                                | 32.2 ms: 1.01x faster                                                    |
| djangocms               | 32.1 us                                                                | 32.7 us: 1.02x slower                                                    |
| docutils                | 2.49 sec                                                               | 2.51 sec: 1.01x slower                                                   |
| fannkuch                | 366 ms                                                                 | 377 ms: 1.03x slower                                                     |
| generators              | 77.4 ms                                                                | 77.0 ms: 1.01x faster                                                    |
| genshi_text             | 20.6 ms                                                                | 20.3 ms: 1.01x faster                                                    |
| genshi_xml              | 47.6 ms                                                                | 46.9 ms: 1.02x faster                                                    |
| go                      | 136 ms                                                                 | 134 ms: 1.01x faster                                                     |
| hexiom                  | 6.10 ms                                                                | 5.96 ms: 1.02x faster                                                    |
| json                    | 4.68 ms                                                                | 4.81 ms: 1.03x slower                                                    |
| json_dumps              | 9.28 ms                                                                | 9.39 ms: 1.01x slower                                                    |
| json_loads              | 23.5 us                                                                | 24.0 us: 1.02x slower                                                    |
| logging_format          | 6.35 us                                                                | 6.26 us: 1.01x faster                                                    |
| logging_simple          | 5.77 us                                                                | 5.72 us: 1.01x faster                                                    |
| mako                    | 9.63 ms                                                                | 9.42 ms: 1.02x faster                                                    |
| mdp                     | 2.51 sec                                                               | 2.56 sec: 1.02x slower                                                   |
| nqueens                 | 78.3 ms                                                                | 77.4 ms: 1.01x faster                                                    |
| pathlib                 | 17.8 ms                                                                | 17.5 ms: 1.02x faster                                                    |
| pickle                  | 10.00 us                                                               | 10.1 us: 1.01x slower                                                    |
| pickle_dict             | 30.6 us                                                                | 30.9 us: 1.01x slower                                                    |
| pickle_list             | 3.97 us                                                                | 4.10 us: 1.03x slower                                                    |
| pickle_pure_python      | 283 us                                                                 | 281 us: 1.00x faster                                                     |
| pidigits                | 192 ms                                                                 | 198 ms: 1.03x slower                                                     |
| pprint_safe_repr        | 675 ms                                                                 | 669 ms: 1.01x faster                                                     |
| pprint_pformat          | 1.38 sec                                                               | 1.37 sec: 1.01x faster                                                   |
| pycparser               | 1.14 sec                                                               | 1.08 sec: 1.05x faster                                                   |
| pyflate                 | 405 ms                                                                 | 407 ms: 1.01x slower                                                     |
| python_startup          | 8.45 ms                                                                | 8.51 ms: 1.01x slower                                                    |
| python_startup_no_site  | 6.06 ms                                                                | 6.09 ms: 1.01x slower                                                    |
| regex_dna               | 208 ms                                                                 | 208 ms: 1.00x faster                                                     |
| regex_v8                | 22.4 ms                                                                | 21.3 ms: 1.05x faster                                                    |
| richards                | 41.5 ms                                                                | 42.0 ms: 1.01x slower                                                    |
| scimark_fft             | 317 ms                                                                 | 310 ms: 1.02x faster                                                     |
| scimark_lu              | 107 ms                                                                 | 105 ms: 1.02x faster                                                     |
| scimark_sor             | 107 ms                                                                 | 105 ms: 1.02x faster                                                     |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 4.01 ms: 1.02x faster                                                    |
| sqlglot_optimize        | 50.6 ms                                                                | 50.3 ms: 1.01x faster                                                    |
| sqlglot_normalize       | 105 ms                                                                 | 103 ms: 1.02x faster                                                     |
| sympy_expand            | 450 ms                                                                 | 457 ms: 1.02x slower                                                     |
| sympy_sum               | 162 ms                                                                 | 163 ms: 1.01x slower                                                     |
| sympy_str               | 281 ms                                                                 | 282 ms: 1.01x slower                                                     |
| telco                   | 6.25 ms                                                                | 6.41 ms: 1.03x slower                                                    |
| thrift                  | 748 us                                                                 | 754 us: 1.01x slower                                                     |
| unpack_sequence         | 42.7 ns                                                                | 42.1 ns: 1.01x faster                                                    |
| unpickle_list           | 5.03 us                                                                | 5.09 us: 1.01x slower                                                    |
| unpickle_pure_python    | 199 us                                                                 | 197 us: 1.01x faster                                                     |
| xml_etree_parse         | 150 ms                                                                 | 148 ms: 1.02x faster                                                     |
| xml_etree_generate      | 76.5 ms                                                                | 76.2 ms: 1.00x faster                                                    |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (25): 2to3, async_tree_none, async_tree_cpu_io_mixed, bench_mp_pool, bench_thread_pool, deltablue, dulwich_log, float, html5lib, logging_silent, meteor_contest, mypy, nbody, raytrace, regex_compile, regex_effbot, scimark_monte_carlo, spectral_norm, sqlglot_parse, sqlglot_transpile, sqlite_synth, sympy_integrate, unpickle, xml_etree_iterparse, xml_etree_process
