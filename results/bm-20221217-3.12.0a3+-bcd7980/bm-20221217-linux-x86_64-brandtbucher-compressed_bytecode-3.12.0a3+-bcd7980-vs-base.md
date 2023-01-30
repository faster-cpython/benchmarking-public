
# Results vs. base

- fork: brandtbucher
- ref: compressed_bytecode
- machine: linux-x86_64
- commit hash: bcd7980
- commit date: 2022-12-17
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 253 ms: 1.00x slower                                                        |
| chameleon      | 6.32 ms                                                                | 6.43 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 192 ms                                                                 | 189 ms: 1.02x faster                                                        |
| nbody          | 94.5 ms                                                                | 93.6 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 22.4 ms                                                                | 22.2 ms: 1.01x faster                                                       |
| regex_effbot   | 3.51 ms                                                                | 3.58 ms: 1.02x slower                                                       |
| regex_dna      | 208 ms                                                                 | 219 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse | 107 ms                                                                 | 102 ms: 1.04x faster                                                        |
| xml_etree_parse     | 150 ms                                                                 | 149 ms: 1.01x faster                                                        |
| xml_etree_generate  | 76.5 ms                                                                | 77.2 ms: 1.01x slower                                                       |
| unpickle_list       | 5.03 us                                                                | 5.12 us: 1.02x slower                                                       |
| json_loads          | 23.5 us                                                                | 24.0 us: 1.02x slower                                                       |
| json_dumps          | 9.28 ms                                                                | 9.49 ms: 1.02x slower                                                       |
| pickle              | 10.00 us                                                               | 10.2 us: 1.03x slower                                                       |
| pickle_list         | 3.97 us                                                                | 4.12 us: 1.04x slower                                                       |
| Geometric mean      | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (5): pickle_pure_python, pickle_dict, unpickle_pure_python, xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.06 ms                                                                | 6.08 ms: 1.00x slower                                                       |
| python_startup         | 8.45 ms                                                                | 8.50 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 47.6 ms                                                                | 47.0 ms: 1.01x faster                                                       |
| mako            | 9.63 ms                                                                | 9.72 ms: 1.01x slower                                                       |
| django_template | 32.4 ms                                                                | 32.9 ms: 1.02x slower                                                       |
| genshi_text     | 20.6 ms                                                                | 21.3 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse     | 107 ms                                                                 | 102 ms: 1.04x faster                                                        |
| chaos                   | 69.0 ms                                                                | 66.1 ms: 1.04x faster                                                       |
| coroutines              | 25.8 ms                                                                | 25.0 ms: 1.04x faster                                                       |
| unpack_sequence         | 42.7 ns                                                                | 41.6 ns: 1.03x faster                                                       |
| async_tree_memoization  | 650 ms                                                                 | 635 ms: 1.02x faster                                                        |
| scimark_sor             | 107 ms                                                                 | 105 ms: 1.02x faster                                                        |
| deepcopy                | 334 us                                                                 | 326 us: 1.02x faster                                                        |
| deepcopy_reduce         | 2.95 us                                                                | 2.88 us: 1.02x faster                                                       |
| meteor_contest          | 106 ms                                                                 | 104 ms: 1.02x faster                                                        |
| pidigits                | 192 ms                                                                 | 189 ms: 1.02x faster                                                        |
| logging_simple          | 5.77 us                                                                | 5.69 us: 1.01x faster                                                       |
| deepcopy_memo           | 33.9 us                                                                | 33.5 us: 1.01x faster                                                       |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 4.03 ms: 1.01x faster                                                       |
| xml_etree_parse         | 150 ms                                                                 | 149 ms: 1.01x faster                                                        |
| telco                   | 6.25 ms                                                                | 6.17 ms: 1.01x faster                                                       |
| genshi_xml              | 47.6 ms                                                                | 47.0 ms: 1.01x faster                                                       |
| logging_format          | 6.35 us                                                                | 6.28 us: 1.01x faster                                                       |
| pathlib                 | 17.8 ms                                                                | 17.6 ms: 1.01x faster                                                       |
| nbody                   | 94.5 ms                                                                | 93.6 ms: 1.01x faster                                                       |
| regex_v8                | 22.4 ms                                                                | 22.2 ms: 1.01x faster                                                       |
| async_tree_io           | 1.33 sec                                                               | 1.32 sec: 1.01x faster                                                      |
| sqlglot_normalize       | 105 ms                                                                 | 104 ms: 1.01x faster                                                        |
| sympy_sum               | 162 ms                                                                 | 161 ms: 1.01x faster                                                        |
| scimark_fft             | 317 ms                                                                 | 315 ms: 1.01x faster                                                        |
| pycparser               | 1.14 sec                                                               | 1.13 sec: 1.01x faster                                                      |
| go                      | 136 ms                                                                 | 135 ms: 1.01x faster                                                        |
| sqlglot_parse           | 1.40 ms                                                                | 1.39 ms: 1.01x faster                                                       |
| sympy_integrate         | 20.3 ms                                                                | 20.2 ms: 1.00x faster                                                       |
| logging_silent          | 92.6 ns                                                                | 92.1 ns: 1.00x faster                                                       |
| crypto_pyaes            | 74.4 ms                                                                | 74.1 ms: 1.00x faster                                                       |
| dulwich_log             | 62.3 ms                                                                | 62.0 ms: 1.00x faster                                                       |
| sqlglot_optimize        | 50.6 ms                                                                | 50.5 ms: 1.00x faster                                                       |
| bench_thread_pool       | 777 us                                                                 | 774 us: 1.00x faster                                                        |
| generators              | 77.4 ms                                                                | 77.6 ms: 1.00x slower                                                       |
| 2to3                    | 252 ms                                                                 | 253 ms: 1.00x slower                                                        |
| python_startup_no_site  | 6.06 ms                                                                | 6.08 ms: 1.00x slower                                                       |
| python_startup          | 8.45 ms                                                                | 8.50 ms: 1.00x slower                                                       |
| pyflate                 | 405 ms                                                                 | 407 ms: 1.01x slower                                                        |
| pprint_pformat          | 1.38 sec                                                               | 1.39 sec: 1.01x slower                                                      |
| xml_etree_generate      | 76.5 ms                                                                | 77.2 ms: 1.01x slower                                                       |
| mako                    | 9.63 ms                                                                | 9.72 ms: 1.01x slower                                                       |
| mdp                     | 2.51 sec                                                               | 2.54 sec: 1.01x slower                                                      |
| spectral_norm           | 94.9 ms                                                                | 96.1 ms: 1.01x slower                                                       |
| chameleon               | 6.32 ms                                                                | 6.43 ms: 1.02x slower                                                       |
| django_template         | 32.4 ms                                                                | 32.9 ms: 1.02x slower                                                       |
| fannkuch                | 366 ms                                                                 | 372 ms: 1.02x slower                                                        |
| djangocms               | 32.1 us                                                                | 32.6 us: 1.02x slower                                                       |
| unpickle_list           | 5.03 us                                                                | 5.12 us: 1.02x slower                                                       |
| regex_effbot            | 3.51 ms                                                                | 3.58 ms: 1.02x slower                                                       |
| json_loads              | 23.5 us                                                                | 24.0 us: 1.02x slower                                                       |
| json_dumps              | 9.28 ms                                                                | 9.49 ms: 1.02x slower                                                       |
| pickle                  | 10.00 us                                                               | 10.2 us: 1.03x slower                                                       |
| json                    | 4.68 ms                                                                | 4.80 ms: 1.03x slower                                                       |
| genshi_text             | 20.6 ms                                                                | 21.3 ms: 1.03x slower                                                       |
| pickle_list             | 3.97 us                                                                | 4.12 us: 1.04x slower                                                       |
| regex_dna               | 208 ms                                                                 | 219 ms: 1.05x slower                                                        |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (28): async_tree_none, sqlite_synth, thrift, sqlglot_transpile, regex_compile, hexiom, scimark_lu, deltablue, pickle_pure_python, sympy_expand, html5lib, pickle_dict, raytrace, bench_mp_pool, mypy, docutils, async_generators, scimark_monte_carlo, async_tree_cpu_io_mixed, unpickle_pure_python, nqueens, sympy_str, richards, pprint_safe_repr, float, xml_etree_process, unpickle, coverage
