
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.02x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 257 ms                                                              | 264 ms: 1.03x slower                                  |
| chameleon      | 6.52 ms                                                             | 6.87 ms: 1.05x slower                                 |
| html5lib       | 64.0 ms                                                             | 65.3 ms: 1.02x slower                                 |
| tornado_http   | 96.7 ms                                                             | 95.4 ms: 1.01x faster                                 |
| Geometric mean | (ref)                                                               | 1.02x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 76.0 ms                                                             | 74.4 ms: 1.02x faster                                 |
| nbody          | 96.7 ms                                                             | 95.2 ms: 1.02x faster                                 |
| Geometric mean | (ref)                                                               | 1.01x faster                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                             | 3.34 ms: 1.00x slower                                 |
| regex_compile  | 137 ms                                                              | 137 ms: 1.01x slower                                  |
| regex_dna      | 196 ms                                                              | 231 ms: 1.18x slower                                  |
| regex_v8       | 22.0 ms                                                             | 25.9 ms: 1.18x slower                                 |
| Geometric mean | (ref)                                                               | 1.09x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 30.9 us                                                             | 27.6 us: 1.12x faster                                 |
| xml_etree_iterparse  | 108 ms                                                              | 104 ms: 1.04x faster                                  |
| xml_etree_parse      | 162 ms                                                              | 157 ms: 1.03x faster                                  |
| pickle               | 9.79 us                                                             | 9.55 us: 1.02x faster                                 |
| json_dumps           | 12.5 ms                                                             | 12.5 ms: 1.00x faster                                 |
| unpickle_pure_python | 228 us                                                              | 231 us: 1.01x slower                                  |
| pickle_pure_python   | 307 us                                                              | 311 us: 1.01x slower                                  |
| xml_etree_process    | 54.1 ms                                                             | 55.2 ms: 1.02x slower                                 |
| xml_etree_generate   | 76.5 ms                                                             | 78.5 ms: 1.03x slower                                 |
| unpickle             | 13.2 us                                                             | 14.1 us: 1.07x slower                                 |
| json_loads           | 26.2 us                                                             | 28.1 us: 1.07x slower                                 |
| pickle_list          | 4.03 us                                                             | 4.57 us: 1.13x slower                                 |
| Geometric mean       | (ref)                                                               | 1.01x slower                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.07 ms: 1.05x faster                                 |
| python_startup_no_site | 5.98 ms                                                             | 5.98 ms: 1.00x slower                                 |
| Geometric mean         | (ref)                                                               | 1.03x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 9.82 ms                                                             | 10.2 ms: 1.04x slower                                 |
| django_template | 32.9 ms                                                             | 34.3 ms: 1.04x slower                                 |
| Geometric mean  | (ref)                                                               | 1.04x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict             | 30.9 us                                                             | 27.6 us: 1.12x faster                                 |
| unpack_sequence         | 49.5 ns                                                             | 44.9 ns: 1.10x faster                                 |
| python_startup          | 8.49 ms                                                             | 8.07 ms: 1.05x faster                                 |
| logging_simple          | 6.09 us                                                             | 5.80 us: 1.05x faster                                 |
| sympy_sum               | 167 ms                                                              | 160 ms: 1.05x faster                                  |
| logging_format          | 6.64 us                                                             | 6.35 us: 1.04x faster                                 |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.04x faster                                  |
| xml_etree_parse         | 162 ms                                                              | 157 ms: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                             | 20.5 ms: 1.03x faster                                 |
| pickle                  | 9.79 us                                                             | 9.55 us: 1.02x faster                                 |
| float                   | 76.0 ms                                                             | 74.4 ms: 1.02x faster                                 |
| nbody                   | 96.7 ms                                                             | 95.2 ms: 1.02x faster                                 |
| sympy_str               | 291 ms                                                              | 287 ms: 1.01x faster                                  |
| tornado_http            | 96.7 ms                                                             | 95.4 ms: 1.01x faster                                 |
| json_dumps              | 12.5 ms                                                             | 12.5 ms: 1.00x faster                                 |
| python_startup_no_site  | 5.98 ms                                                             | 5.98 ms: 1.00x slower                                 |
| regex_effbot            | 3.32 ms                                                             | 3.34 ms: 1.00x slower                                 |
| regex_compile           | 137 ms                                                              | 137 ms: 1.01x slower                                  |
| unpickle_pure_python    | 228 us                                                              | 231 us: 1.01x slower                                  |
| deltablue               | 3.66 ms                                                             | 3.70 ms: 1.01x slower                                 |
| pathlib                 | 18.2 ms                                                             | 18.5 ms: 1.01x slower                                 |
| pickle_pure_python      | 307 us                                                              | 311 us: 1.01x slower                                  |
| nqueens                 | 84.0 ms                                                             | 85.2 ms: 1.01x slower                                 |
| html5lib                | 64.0 ms                                                             | 65.3 ms: 1.02x slower                                 |
| xml_etree_process       | 54.1 ms                                                             | 55.2 ms: 1.02x slower                                 |
| scimark_fft             | 328 ms                                                              | 335 ms: 1.02x slower                                  |
| xml_etree_generate      | 76.5 ms                                                             | 78.5 ms: 1.03x slower                                 |
| 2to3                    | 257 ms                                                              | 264 ms: 1.03x slower                                  |
| go                      | 138 ms                                                              | 143 ms: 1.03x slower                                  |
| chaos                   | 68.0 ms                                                             | 70.2 ms: 1.03x slower                                 |
| mako                    | 9.82 ms                                                             | 10.2 ms: 1.04x slower                                 |
| richards                | 45.7 ms                                                             | 47.5 ms: 1.04x slower                                 |
| django_template         | 32.9 ms                                                             | 34.3 ms: 1.04x slower                                 |
| json                    | 4.86 ms                                                             | 5.07 ms: 1.04x slower                                 |
| fannkuch                | 384 ms                                                              | 401 ms: 1.04x slower                                  |
| scimark_monte_carlo     | 67.8 ms                                                             | 70.8 ms: 1.04x slower                                 |
| raytrace                | 292 ms                                                              | 306 ms: 1.05x slower                                  |
| spectral_norm           | 99.5 ms                                                             | 105 ms: 1.05x slower                                  |
| logging_silent          | 98.7 ns                                                             | 104 ns: 1.05x slower                                  |
| chameleon               | 6.52 ms                                                             | 6.87 ms: 1.05x slower                                 |
| hexiom                  | 6.48 ms                                                             | 6.84 ms: 1.05x slower                                 |
| pyflate                 | 414 ms                                                              | 438 ms: 1.06x slower                                  |
| unpickle                | 13.2 us                                                             | 14.1 us: 1.07x slower                                 |
| scimark_sor             | 115 ms                                                              | 123 ms: 1.07x slower                                  |
| json_loads              | 26.2 us                                                             | 28.1 us: 1.07x slower                                 |
| pycparser               | 1.14 sec                                                            | 1.24 sec: 1.08x slower                                |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.85 ms: 1.09x slower                                 |
| crypto_pyaes            | 73.8 ms                                                             | 82.7 ms: 1.12x slower                                 |
| pickle_list             | 4.03 us                                                             | 4.57 us: 1.13x slower                                 |
| regex_dna               | 196 ms                                                              | 231 ms: 1.18x slower                                  |
| regex_v8                | 22.0 ms                                                             | 25.9 ms: 1.18x slower                                 |
| Geometric mean          | (ref)                                                               | 1.02x slower                                          |

Benchmark hidden because not significant (9): thrift, sqlite_synth, scimark_lu, sympy_expand, pidigits, telco, unpickle_list, dulwich_log, meteor_contest
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
