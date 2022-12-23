Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 253 ms: 1.00x slower                                                     |
| chameleon      | 6.32 ms                                                                | 6.54 ms: 1.03x slower                                                    |
| docutils       | 2.49 sec                                                               | 2.55 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 72.0 ms                                                                | 73.2 ms: 1.02x slower                                                    |
| pidigits       | 192 ms                                                                 | 193 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 208 ms                                                                 | 204 ms: 1.02x faster                                                     |
| regex_effbot   | 3.51 ms                                                                | 3.43 ms: 1.02x faster                                                    |
| regex_v8       | 22.4 ms                                                                | 21.9 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|--------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads         | 23.5 us                                                                | 24.1 us: 1.03x slower                                                    |
| pickle             | 10.00 us                                                               | 10.1 us: 1.01x slower                                                    |
| pickle_dict        | 30.6 us                                                                | 31.2 us: 1.02x slower                                                    |
| pickle_list        | 3.97 us                                                                | 4.11 us: 1.03x slower                                                    |
| pickle_pure_python | 283 us                                                                 | 278 us: 1.02x faster                                                     |
| unpickle_list      | 5.03 us                                                                | 5.01 us: 1.00x faster                                                    |
| xml_etree_parse    | 150 ms                                                                 | 148 ms: 1.02x faster                                                     |
| xml_etree_generate | 76.5 ms                                                                | 78.1 ms: 1.02x slower                                                    |
| xml_etree_process  | 53.4 ms                                                                | 54.0 ms: 1.01x slower                                                    |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (4): json_dumps, unpickle, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.45 ms                                                                | 8.56 ms: 1.01x slower                                                    |
| python_startup_no_site | 6.06 ms                                                                | 6.12 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 9.63 ms                                                                | 9.51 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3                    | 252 ms                                                                 | 253 ms: 1.00x slower                                                     |
| async_generators        | 354 ms                                                                 | 349 ms: 1.02x faster                                                     |
| chameleon               | 6.32 ms                                                                | 6.54 ms: 1.03x slower                                                    |
| chaos                   | 69.0 ms                                                                | 66.4 ms: 1.04x faster                                                    |
| coroutines              | 25.8 ms                                                                | 24.8 ms: 1.04x faster                                                    |
| coverage                | 98.7 ms                                                                | 97.5 ms: 1.01x faster                                                    |
| crypto_pyaes            | 74.4 ms                                                                | 75.9 ms: 1.02x slower                                                    |
| deepcopy                | 334 us                                                                 | 322 us: 1.04x faster                                                     |
| deepcopy_reduce         | 2.95 us                                                                | 2.89 us: 1.02x faster                                                    |
| deepcopy_memo           | 33.9 us                                                                | 32.9 us: 1.03x faster                                                    |
| deltablue               | 3.23 ms                                                                | 3.24 ms: 1.00x slower                                                    |
| djangocms               | 32.1 us                                                                | 32.8 us: 1.02x slower                                                    |
| docutils                | 2.49 sec                                                               | 2.55 sec: 1.02x slower                                                   |
| dulwich_log             | 62.3 ms                                                                | 62.5 ms: 1.00x slower                                                    |
| float                   | 72.0 ms                                                                | 73.2 ms: 1.02x slower                                                    |
| generators              | 77.4 ms                                                                | 74.8 ms: 1.04x faster                                                    |
| go                      | 136 ms                                                                 | 132 ms: 1.03x faster                                                     |
| json                    | 4.68 ms                                                                | 5.03 ms: 1.08x slower                                                    |
| json_loads              | 23.5 us                                                                | 24.1 us: 1.03x slower                                                    |
| logging_format          | 6.35 us                                                                | 6.22 us: 1.02x faster                                                    |
| logging_silent          | 92.6 ns                                                                | 91.2 ns: 1.01x faster                                                    |
| logging_simple          | 5.77 us                                                                | 5.63 us: 1.02x faster                                                    |
| mako                    | 9.63 ms                                                                | 9.51 ms: 1.01x faster                                                    |
| mdp                     | 2.51 sec                                                               | 2.71 sec: 1.08x slower                                                   |
| meteor_contest          | 106 ms                                                                 | 108 ms: 1.02x slower                                                     |
| pickle                  | 10.00 us                                                               | 10.1 us: 1.01x slower                                                    |
| pickle_dict             | 30.6 us                                                                | 31.2 us: 1.02x slower                                                    |
| pickle_list             | 3.97 us                                                                | 4.11 us: 1.03x slower                                                    |
| pickle_pure_python      | 283 us                                                                 | 278 us: 1.02x faster                                                     |
| pidigits                | 192 ms                                                                 | 193 ms: 1.00x slower                                                     |
| pprint_safe_repr        | 675 ms                                                                 | 666 ms: 1.01x faster                                                     |
| pprint_pformat          | 1.38 sec                                                               | 1.37 sec: 1.01x faster                                                   |
| pycparser               | 1.14 sec                                                               | 1.10 sec: 1.03x faster                                                   |
| pyflate                 | 405 ms                                                                 | 397 ms: 1.02x faster                                                     |
| python_startup          | 8.45 ms                                                                | 8.56 ms: 1.01x slower                                                    |
| python_startup_no_site  | 6.06 ms                                                                | 6.12 ms: 1.01x slower                                                    |
| regex_dna               | 208 ms                                                                 | 204 ms: 1.02x faster                                                     |
| regex_effbot            | 3.51 ms                                                                | 3.43 ms: 1.02x faster                                                    |
| regex_v8                | 22.4 ms                                                                | 21.9 ms: 1.02x faster                                                    |
| richards                | 41.5 ms                                                                | 41.9 ms: 1.01x slower                                                    |
| scimark_fft             | 317 ms                                                                 | 316 ms: 1.00x faster                                                     |
| scimark_sor             | 107 ms                                                                 | 107 ms: 1.01x faster                                                     |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 4.27 ms: 1.04x slower                                                    |
| spectral_norm           | 94.9 ms                                                                | 95.8 ms: 1.01x slower                                                    |
| sqlglot_parse           | 1.40 ms                                                                | 1.42 ms: 1.01x slower                                                    |
| sqlglot_transpile       | 1.69 ms                                                                | 1.71 ms: 1.01x slower                                                    |
| sqlglot_normalize       | 105 ms                                                                 | 104 ms: 1.00x faster                                                     |
| sympy_expand            | 450 ms                                                                 | 453 ms: 1.01x slower                                                     |
| sympy_integrate         | 20.3 ms                                                                | 20.5 ms: 1.01x slower                                                    |
| sympy_sum               | 162 ms                                                                 | 164 ms: 1.01x slower                                                     |
| sympy_str               | 281 ms                                                                 | 283 ms: 1.01x slower                                                     |
| unpack_sequence         | 42.7 ns                                                                | 42.1 ns: 1.01x faster                                                    |
| unpickle_list           | 5.03 us                                                                | 5.01 us: 1.00x faster                                                    |
| xml_etree_parse         | 150 ms                                                                 | 148 ms: 1.02x faster                                                     |
| xml_etree_generate      | 76.5 ms                                                                | 78.1 ms: 1.02x slower                                                    |
| xml_etree_process       | 53.4 ms                                                                | 54.0 ms: 1.01x slower                                                    |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (28): async_tree_none, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, bench_mp_pool, bench_thread_pool, django_template, fannkuch, genshi_text, genshi_xml, hexiom, html5lib, json_dumps, mypy, nbody, nqueens, pathlib, raytrace, regex_compile, scimark_lu, scimark_monte_carlo, sqlglot_optimize, sqlite_synth, telco, thrift, unpickle, unpickle_pure_python, xml_etree_iterparse
