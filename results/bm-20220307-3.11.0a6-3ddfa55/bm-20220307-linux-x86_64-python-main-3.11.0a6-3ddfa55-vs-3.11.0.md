
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3ddfa55
- commit date: 2022-03-07
- overall geometric mean: 1.06x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 257 ms                                                              | 268 ms: 1.04x slower                                  |
| chameleon      | 6.52 ms                                                             | 6.93 ms: 1.06x slower                                 |
| html5lib       | 64.0 ms                                                             | 68.6 ms: 1.07x slower                                 |
| tornado_http   | 96.7 ms                                                             | 99.2 ms: 1.03x slower                                 |
| Geometric mean | (ref)                                                               | 1.05x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 97.7 ms: 1.01x slower                                 |
| float          | 76.0 ms                                                             | 78.7 ms: 1.04x slower                                 |
| pidigits       | 197 ms                                                              | 208 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                               | 1.03x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 140 ms: 1.02x slower                                  |
| regex_v8       | 22.0 ms                                                             | 23.0 ms: 1.05x slower                                 |
| regex_effbot   | 3.32 ms                                                             | 3.49 ms: 1.05x slower                                 |
| regex_dna      | 196 ms                                                              | 221 ms: 1.12x slower                                  |
| Geometric mean | (ref)                                                               | 1.06x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 30.9 us                                                             | 28.1 us: 1.10x faster                                 |
| xml_etree_parse      | 162 ms                                                              | 156 ms: 1.04x faster                                  |
| xml_etree_iterparse  | 108 ms                                                              | 105 ms: 1.03x faster                                  |
| pickle               | 9.79 us                                                             | 9.69 us: 1.01x faster                                 |
| unpickle_list        | 4.96 us                                                             | 4.92 us: 1.01x faster                                 |
| json_dumps           | 12.5 ms                                                             | 12.6 ms: 1.01x slower                                 |
| xml_etree_process    | 54.1 ms                                                             | 56.0 ms: 1.04x slower                                 |
| xml_etree_generate   | 76.5 ms                                                             | 79.6 ms: 1.04x slower                                 |
| unpickle             | 13.2 us                                                             | 14.2 us: 1.07x slower                                 |
| json_loads           | 26.2 us                                                             | 28.1 us: 1.07x slower                                 |
| unpickle_pure_python | 228 us                                                              | 246 us: 1.08x slower                                  |
| pickle_pure_python   | 307 us                                                              | 335 us: 1.09x slower                                  |
| pickle_list          | 4.03 us                                                             | 4.51 us: 1.12x slower                                 |
| Geometric mean       | (ref)                                                               | 1.02x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.20 ms: 1.04x faster                                 |
| python_startup_no_site | 5.98 ms                                                             | 6.07 ms: 1.02x slower                                 |
| Geometric mean         | (ref)                                                               | 1.01x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 9.82 ms                                                             | 10.6 ms: 1.08x slower                                 |
| django_template | 32.9 ms                                                             | 36.0 ms: 1.09x slower                                 |
| Geometric mean  | (ref)                                                               | 1.09x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| logging_simple          | 6.09 us                                                             | 5.52 us: 1.10x faster                                 |
| pickle_dict             | 30.9 us                                                             | 28.1 us: 1.10x faster                                 |
| logging_format          | 6.64 us                                                             | 6.08 us: 1.09x faster                                 |
| python_startup          | 8.49 ms                                                             | 8.20 ms: 1.04x faster                                 |
| xml_etree_parse         | 162 ms                                                              | 156 ms: 1.04x faster                                  |
| sympy_sum               | 167 ms                                                              | 163 ms: 1.03x faster                                  |
| xml_etree_iterparse     | 108 ms                                                              | 105 ms: 1.03x faster                                  |
| pickle                  | 9.79 us                                                             | 9.69 us: 1.01x faster                                 |
| sympy_integrate         | 21.0 ms                                                             | 20.9 ms: 1.01x faster                                 |
| unpickle_list           | 4.96 us                                                             | 4.92 us: 1.01x faster                                 |
| sympy_str               | 291 ms                                                              | 289 ms: 1.01x faster                                  |
| json_dumps              | 12.5 ms                                                             | 12.6 ms: 1.01x slower                                 |
| sympy_expand            | 477 ms                                                              | 481 ms: 1.01x slower                                  |
| nbody                   | 96.7 ms                                                             | 97.7 ms: 1.01x slower                                 |
| python_startup_no_site  | 5.98 ms                                                             | 6.07 ms: 1.02x slower                                 |
| regex_compile           | 137 ms                                                              | 140 ms: 1.02x slower                                  |
| tornado_http            | 96.7 ms                                                             | 99.2 ms: 1.03x slower                                 |
| scimark_fft             | 328 ms                                                              | 336 ms: 1.03x slower                                  |
| json                    | 4.86 ms                                                             | 5.00 ms: 1.03x slower                                 |
| thrift                  | 766 us                                                              | 789 us: 1.03x slower                                  |
| xml_etree_process       | 54.1 ms                                                             | 56.0 ms: 1.04x slower                                 |
| float                   | 76.0 ms                                                             | 78.7 ms: 1.04x slower                                 |
| nqueens                 | 84.0 ms                                                             | 87.0 ms: 1.04x slower                                 |
| fannkuch                | 384 ms                                                              | 398 ms: 1.04x slower                                  |
| xml_etree_generate      | 76.5 ms                                                             | 79.6 ms: 1.04x slower                                 |
| 2to3                    | 257 ms                                                              | 268 ms: 1.04x slower                                  |
| dulwich_log             | 63.6 ms                                                             | 66.5 ms: 1.05x slower                                 |
| regex_v8                | 22.0 ms                                                             | 23.0 ms: 1.05x slower                                 |
| regex_effbot            | 3.32 ms                                                             | 3.49 ms: 1.05x slower                                 |
| telco                   | 6.59 ms                                                             | 6.92 ms: 1.05x slower                                 |
| pidigits                | 197 ms                                                              | 208 ms: 1.06x slower                                  |
| pycparser               | 1.14 sec                                                            | 1.21 sec: 1.06x slower                                |
| richards                | 45.7 ms                                                             | 48.5 ms: 1.06x slower                                 |
| chameleon               | 6.52 ms                                                             | 6.93 ms: 1.06x slower                                 |
| scimark_lu              | 108 ms                                                              | 115 ms: 1.06x slower                                  |
| go                      | 138 ms                                                              | 148 ms: 1.07x slower                                  |
| html5lib                | 64.0 ms                                                             | 68.6 ms: 1.07x slower                                 |
| unpickle                | 13.2 us                                                             | 14.2 us: 1.07x slower                                 |
| json_loads              | 26.2 us                                                             | 28.1 us: 1.07x slower                                 |
| scimark_monte_carlo     | 67.8 ms                                                             | 72.9 ms: 1.08x slower                                 |
| scimark_sor             | 115 ms                                                              | 123 ms: 1.08x slower                                  |
| unpickle_pure_python    | 228 us                                                              | 246 us: 1.08x slower                                  |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.82 ms: 1.08x slower                                 |
| mako                    | 9.82 ms                                                             | 10.6 ms: 1.08x slower                                 |
| spectral_norm           | 99.5 ms                                                             | 107 ms: 1.08x slower                                  |
| chaos                   | 68.0 ms                                                             | 73.5 ms: 1.08x slower                                 |
| hexiom                  | 6.48 ms                                                             | 7.04 ms: 1.09x slower                                 |
| raytrace                | 292 ms                                                              | 318 ms: 1.09x slower                                  |
| pickle_pure_python      | 307 us                                                              | 335 us: 1.09x slower                                  |
| django_template         | 32.9 ms                                                             | 36.0 ms: 1.09x slower                                 |
| pyflate                 | 414 ms                                                              | 453 ms: 1.10x slower                                  |
| pickle_list             | 4.03 us                                                             | 4.51 us: 1.12x slower                                 |
| regex_dna               | 196 ms                                                              | 221 ms: 1.12x slower                                  |
| deltablue               | 3.66 ms                                                             | 4.16 ms: 1.14x slower                                 |
| logging_silent          | 98.7 ns                                                             | 113 ns: 1.14x slower                                  |
| crypto_pyaes            | 73.8 ms                                                             | 84.6 ms: 1.15x slower                                 |
| unpack_sequence         | 49.5 ns                                                             | 131 ns: 2.65x slower                                  |
| Geometric mean          | (ref)                                                               | 1.06x slower                                          |

Benchmark hidden because not significant (3): meteor_contest, sqlite_synth, pathlib
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
