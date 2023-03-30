
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 257 ms                                                              | 256 ms: 1.00x faster                                  |
| chameleon      | 6.52 ms                                                             | 6.59 ms: 1.01x slower                                 |
| tornado_http   | 96.7 ms                                                             | 93.8 ms: 1.03x faster                                 |
| Geometric mean | (ref)                                                               | 1.01x faster                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 90.9 ms: 1.06x faster                                 |
| float          | 76.0 ms                                                             | 72.8 ms: 1.04x faster                                 |
| pidigits       | 197 ms                                                              | 190 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                               | 1.05x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                             | 3.02 ms: 1.10x faster                                 |
| regex_v8       | 22.0 ms                                                             | 21.5 ms: 1.02x faster                                 |
| Geometric mean | (ref)                                                               | 1.03x faster                                          |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 30.9 us                                                             | 25.9 us: 1.19x faster                                 |
| json_loads           | 26.2 us                                                             | 24.3 us: 1.08x faster                                 |
| xml_etree_iterparse  | 108 ms                                                              | 104 ms: 1.04x faster                                  |
| xml_etree_parse      | 162 ms                                                              | 157 ms: 1.03x faster                                  |
| pickle               | 9.79 us                                                             | 9.61 us: 1.02x faster                                 |
| pickle_pure_python   | 307 us                                                              | 302 us: 1.02x faster                                  |
| xml_etree_process    | 54.1 ms                                                             | 53.3 ms: 1.02x faster                                 |
| xml_etree_generate   | 76.5 ms                                                             | 75.8 ms: 1.01x faster                                 |
| unpickle_pure_python | 228 us                                                              | 227 us: 1.00x faster                                  |
| unpickle             | 13.2 us                                                             | 13.3 us: 1.01x slower                                 |
| pickle_list          | 4.03 us                                                             | 4.30 us: 1.07x slower                                 |
| Geometric mean       | (ref)                                                               | 1.02x faster                                          |

Benchmark hidden because not significant (2): json_dumps, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.33 ms: 1.02x faster                                 |
| python_startup_no_site | 5.98 ms                                                             | 6.17 ms: 1.03x slower                                 |
| Geometric mean         | (ref)                                                               | 1.01x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 32.9 ms                                                             | 32.4 ms: 1.02x faster                                 |
| mako            | 9.82 ms                                                             | 9.71 ms: 1.01x faster                                 |
| Geometric mean  | (ref)                                                               | 1.01x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict             | 30.9 us                                                             | 25.9 us: 1.19x faster                                 |
| unpack_sequence         | 49.5 ns                                                             | 43.2 ns: 1.15x faster                                 |
| regex_effbot            | 3.32 ms                                                             | 3.02 ms: 1.10x faster                                 |
| json_loads              | 26.2 us                                                             | 24.3 us: 1.08x faster                                 |
| nbody                   | 96.7 ms                                                             | 90.9 ms: 1.06x faster                                 |
| sympy_sum               | 167 ms                                                              | 159 ms: 1.05x faster                                  |
| logging_simple          | 6.09 us                                                             | 5.82 us: 1.05x faster                                 |
| float                   | 76.0 ms                                                             | 72.8 ms: 1.04x faster                                 |
| pidigits                | 197 ms                                                              | 190 ms: 1.04x faster                                  |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.04x faster                                  |
| pycparser               | 1.14 sec                                                            | 1.10 sec: 1.04x faster                                |
| logging_format          | 6.64 us                                                             | 6.42 us: 1.03x faster                                 |
| spectral_norm           | 99.5 ms                                                             | 96.3 ms: 1.03x faster                                 |
| xml_etree_parse         | 162 ms                                                              | 157 ms: 1.03x faster                                  |
| tornado_http            | 96.7 ms                                                             | 93.8 ms: 1.03x faster                                 |
| sympy_integrate         | 21.0 ms                                                             | 20.5 ms: 1.03x faster                                 |
| json                    | 4.86 ms                                                             | 4.72 ms: 1.03x faster                                 |
| sympy_expand            | 477 ms                                                              | 465 ms: 1.03x faster                                  |
| sympy_str               | 291 ms                                                              | 284 ms: 1.02x faster                                  |
| hexiom                  | 6.48 ms                                                             | 6.32 ms: 1.02x faster                                 |
| scimark_monte_carlo     | 67.8 ms                                                             | 66.5 ms: 1.02x faster                                 |
| regex_v8                | 22.0 ms                                                             | 21.5 ms: 1.02x faster                                 |
| python_startup          | 8.49 ms                                                             | 8.33 ms: 1.02x faster                                 |
| nqueens                 | 84.0 ms                                                             | 82.4 ms: 1.02x faster                                 |
| pickle                  | 9.79 us                                                             | 9.61 us: 1.02x faster                                 |
| meteor_contest          | 106 ms                                                              | 104 ms: 1.02x faster                                  |
| dulwich_log             | 63.6 ms                                                             | 62.6 ms: 1.02x faster                                 |
| django_template         | 32.9 ms                                                             | 32.4 ms: 1.02x faster                                 |
| deltablue               | 3.66 ms                                                             | 3.60 ms: 1.02x faster                                 |
| pickle_pure_python      | 307 us                                                              | 302 us: 1.02x faster                                  |
| xml_etree_process       | 54.1 ms                                                             | 53.3 ms: 1.02x faster                                 |
| go                      | 138 ms                                                              | 136 ms: 1.01x faster                                  |
| thrift                  | 766 us                                                              | 756 us: 1.01x faster                                  |
| scimark_fft             | 328 ms                                                              | 324 ms: 1.01x faster                                  |
| mako                    | 9.82 ms                                                             | 9.71 ms: 1.01x faster                                 |
| pyflate                 | 414 ms                                                              | 410 ms: 1.01x faster                                  |
| scimark_lu              | 108 ms                                                              | 107 ms: 1.01x faster                                  |
| xml_etree_generate      | 76.5 ms                                                             | 75.8 ms: 1.01x faster                                 |
| logging_silent          | 98.7 ns                                                             | 98.1 ns: 1.01x faster                                 |
| unpickle_pure_python    | 228 us                                                              | 227 us: 1.00x faster                                  |
| 2to3                    | 257 ms                                                              | 256 ms: 1.00x faster                                  |
| unpickle                | 13.2 us                                                             | 13.3 us: 1.01x slower                                 |
| chameleon               | 6.52 ms                                                             | 6.59 ms: 1.01x slower                                 |
| fannkuch                | 384 ms                                                              | 394 ms: 1.03x slower                                  |
| python_startup_no_site  | 5.98 ms                                                             | 6.17 ms: 1.03x slower                                 |
| pickle_list             | 4.03 us                                                             | 4.30 us: 1.07x slower                                 |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.79 ms: 1.07x slower                                 |
| Geometric mean          | (ref)                                                               | 1.02x faster                                          |

Benchmark hidden because not significant (13): richards, sqlite_synth, html5lib, raytrace, chaos, regex_compile, regex_dna, crypto_pyaes, scimark_sor, pathlib, json_dumps, unpickle_list, telco
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
