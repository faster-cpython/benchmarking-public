
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b2
- machine: linux-x86_64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 289 ms                                                                    | 282 ms: 1.03x faster                                             |
| docutils       | 2.86 sec                                                                  | 2.83 sec: 1.01x faster                                           |
| tornado_http   | 125 ms                                                                    | 117 ms: 1.06x faster                                             |
| Geometric mean | (ref)                                                                     | 1.02x faster                                                     |

Benchmark hidden because not significant (2): chameleon, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 75.7 ms                                                                   | 73.8 ms: 1.03x faster                                            |
| nbody          | 92.1 ms                                                                   | 96.9 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                                     | 1.01x slower                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.31 ms                                                                   | 3.11 ms: 1.06x faster                                            |
| regex_v8       | 24.4 ms                                                                   | 24.1 ms: 1.01x faster                                            |
| regex_dna      | 225 ms                                                                    | 227 ms: 1.01x slower                                             |
| regex_compile  | 154 ms                                                                    | 157 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                                     | 1.01x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_loads           | 28.4 us                                                                   | 25.1 us: 1.13x faster                                            |
| xml_etree_parse      | 161 ms                                                                    | 153 ms: 1.05x faster                                             |
| pickle_dict          | 31.1 us                                                                   | 30.4 us: 1.02x faster                                            |
| unpickle_pure_python | 238 us                                                                    | 234 us: 1.02x faster                                             |
| pickle               | 9.92 us                                                                   | 9.77 us: 1.01x faster                                            |
| unpickle_list        | 4.52 us                                                                   | 4.57 us: 1.01x slower                                            |
| unpickle             | 13.0 us                                                                   | 13.3 us: 1.02x slower                                            |
| pickle_list          | 3.78 us                                                                   | 3.86 us: 1.02x slower                                            |
| Geometric mean       | (ref)                                                                     | 1.01x faster                                                     |

Benchmark hidden because not significant (5): json_dumps, xml_etree_generate, xml_etree_process, xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|------------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                                   | 10.7 ms: 1.01x faster                                            |
| python_startup_no_site | 7.73 ms                                                                   | 7.70 ms: 1.00x faster                                            |
| Geometric mean         | (ref)                                                                     | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text    | 26.3 ms                                                                   | 24.4 ms: 1.08x faster                                            |
| genshi_xml     | 57.8 ms                                                                   | 56.0 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                                     | 1.03x faster                                                     |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_loads              | 28.4 us                                                                   | 25.1 us: 1.13x faster                                            |
| json                    | 5.59 ms                                                                   | 5.16 ms: 1.08x faster                                            |
| genshi_text             | 26.3 ms                                                                   | 24.4 ms: 1.08x faster                                            |
| gc_traversal            | 4.22 ms                                                                   | 3.94 ms: 1.07x faster                                            |
| tornado_http            | 125 ms                                                                    | 117 ms: 1.06x faster                                             |
| regex_effbot            | 3.31 ms                                                                   | 3.11 ms: 1.06x faster                                            |
| chaos                   | 76.2 ms                                                                   | 72.1 ms: 1.06x faster                                            |
| coroutines              | 29.5 ms                                                                   | 27.9 ms: 1.06x faster                                            |
| async_tree_memoization  | 639 ms                                                                    | 609 ms: 1.05x faster                                             |
| xml_etree_parse         | 161 ms                                                                    | 153 ms: 1.05x faster                                             |
| logging_silent          | 103 ns                                                                    | 98.9 ns: 1.04x faster                                            |
| async_tree_none         | 529 ms                                                                    | 511 ms: 1.03x faster                                             |
| nqueens                 | 101 ms                                                                    | 97.7 ms: 1.03x faster                                            |
| genshi_xml              | 57.8 ms                                                                   | 56.0 ms: 1.03x faster                                            |
| sympy_sum               | 182 ms                                                                    | 177 ms: 1.03x faster                                             |
| dulwich_log             | 69.1 ms                                                                   | 67.2 ms: 1.03x faster                                            |
| float                   | 75.7 ms                                                                   | 73.8 ms: 1.03x faster                                            |
| 2to3                    | 289 ms                                                                    | 282 ms: 1.03x faster                                             |
| scimark_lu              | 114 ms                                                                    | 111 ms: 1.03x faster                                             |
| sympy_expand            | 547 ms                                                                    | 533 ms: 1.02x faster                                             |
| go                      | 158 ms                                                                    | 154 ms: 1.02x faster                                             |
| sqlalchemy_imperative   | 19.8 ms                                                                   | 19.4 ms: 1.02x faster                                            |
| pickle_dict             | 31.1 us                                                                   | 30.4 us: 1.02x faster                                            |
| dask                    | 418 ms                                                                    | 410 ms: 1.02x faster                                             |
| sympy_str               | 333 ms                                                                    | 327 ms: 1.02x faster                                             |
| pprint_pformat          | 1.60 sec                                                                  | 1.57 sec: 1.02x faster                                           |
| spectral_norm           | 95.1 ms                                                                   | 93.4 ms: 1.02x faster                                            |
| async_tree_cpu_io_mixed | 754 ms                                                                    | 740 ms: 1.02x faster                                             |
| crypto_pyaes            | 85.0 ms                                                                   | 83.5 ms: 1.02x faster                                            |
| unpickle_pure_python    | 238 us                                                                    | 234 us: 1.02x faster                                             |
| unpack_sequence         | 45.9 ns                                                                   | 45.1 ns: 1.02x faster                                            |
| sqlalchemy_declarative  | 156 ms                                                                    | 153 ms: 1.02x faster                                             |
| async_generators        | 318 ms                                                                    | 313 ms: 1.02x faster                                             |
| async_tree_io           | 1.18 sec                                                                  | 1.16 sec: 1.02x faster                                           |
| pyflate                 | 438 ms                                                                    | 431 ms: 1.02x faster                                             |
| aiohttp                 | 959 us                                                                    | 944 us: 1.02x faster                                             |
| pickle                  | 9.92 us                                                                   | 9.77 us: 1.01x faster                                            |
| scimark_sor             | 109 ms                                                                    | 108 ms: 1.01x faster                                             |
| pylint                  | 517 ms                                                                    | 510 ms: 1.01x faster                                             |
| generators              | 56.0 ms                                                                   | 55.2 ms: 1.01x faster                                            |
| regex_v8                | 24.4 ms                                                                   | 24.1 ms: 1.01x faster                                            |
| richards                | 49.1 ms                                                                   | 48.5 ms: 1.01x faster                                            |
| pprint_safe_repr        | 768 ms                                                                    | 759 ms: 1.01x faster                                             |
| docutils                | 2.86 sec                                                                  | 2.83 sec: 1.01x faster                                           |
| sympy_integrate         | 25.3 ms                                                                   | 25.0 ms: 1.01x faster                                            |
| asyncio_tcp             | 752 ms                                                                    | 746 ms: 1.01x faster                                             |
| gunicorn                | 936 us                                                                    | 929 us: 1.01x faster                                             |
| python_startup          | 10.7 ms                                                                   | 10.7 ms: 1.01x faster                                            |
| pathlib                 | 19.2 ms                                                                   | 19.1 ms: 1.01x faster                                            |
| python_startup_no_site  | 7.73 ms                                                                   | 7.70 ms: 1.00x faster                                            |
| raytrace                | 303 ms                                                                    | 305 ms: 1.01x slower                                             |
| regex_dna               | 225 ms                                                                    | 227 ms: 1.01x slower                                             |
| unpickle_list           | 4.52 us                                                                   | 4.57 us: 1.01x slower                                            |
| sqlglot_normalize       | 122 ms                                                                    | 124 ms: 1.02x slower                                             |
| unpickle                | 13.0 us                                                                   | 13.3 us: 1.02x slower                                            |
| regex_compile           | 154 ms                                                                    | 157 ms: 1.02x slower                                             |
| sqlglot_optimize        | 58.6 ms                                                                   | 59.7 ms: 1.02x slower                                            |
| pickle_list             | 3.78 us                                                                   | 3.86 us: 1.02x slower                                            |
| sqlite_synth            | 2.49 us                                                                   | 2.54 us: 1.02x slower                                            |
| deepcopy_reduce         | 3.39 us                                                                   | 3.47 us: 1.02x slower                                            |
| scimark_fft             | 276 ms                                                                    | 284 ms: 1.03x slower                                             |
| logging_simple          | 6.95 us                                                                   | 7.21 us: 1.04x slower                                            |
| telco                   | 6.70 ms                                                                   | 6.99 ms: 1.04x slower                                            |
| mdp                     | 2.73 sec                                                                  | 2.85 sec: 1.04x slower                                           |
| nbody                   | 92.1 ms                                                                   | 96.9 ms: 1.05x slower                                            |
| comprehensions          | 24.7 us                                                                   | 27.9 us: 1.13x slower                                            |
| sqlglot_transpile       | 1.88 ms                                                                   | 2.29 ms: 1.22x slower                                            |
| sqlglot_parse           | 1.53 ms                                                                   | 1.95 ms: 1.27x slower                                            |
| Geometric mean          | (ref)                                                                     | 1.01x faster                                                     |

Benchmark hidden because not significant (25): mypy2, thrift, scimark_monte_carlo, fannkuch, logging_format, deltablue, django_template, json_dumps, hexiom, deepcopy_memo, xml_etree_generate, pycparser, create_gc_cycles, scimark_sparse_mat_mult, meteor_contest, pidigits, xml_etree_process, xml_etree_iterparse, bench_mp_pool, chameleon, pickle_pure_python, deepcopy, mako, html5lib, bench_thread_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: coverage, flaskblogging
