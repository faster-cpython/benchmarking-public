
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2e91dba
- commit date: 2021-12-08
- overall geometric mean: 1.06x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 257 ms                                                              | 264 ms: 1.03x slower                                  |
| chameleon      | 6.52 ms                                                             | 7.44 ms: 1.14x slower                                 |
| html5lib       | 64.0 ms                                                             | 68.5 ms: 1.07x slower                                 |
| tornado_http   | 96.7 ms                                                             | 108 ms: 1.11x slower                                  |
| Geometric mean | (ref)                                                               | 1.09x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 96.1 ms: 1.01x faster                                 |
| pidigits       | 197 ms                                                              | 198 ms: 1.01x slower                                  |
| float          | 76.0 ms                                                             | 79.2 ms: 1.04x slower                                 |
| Geometric mean | (ref)                                                               | 1.01x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                             | 3.21 ms: 1.03x faster                                 |
| regex_compile  | 137 ms                                                              | 139 ms: 1.02x slower                                  |
| regex_dna      | 196 ms                                                              | 212 ms: 1.08x slower                                  |
| regex_v8       | 22.0 ms                                                             | 24.5 ms: 1.12x slower                                 |
| Geometric mean | (ref)                                                               | 1.04x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 30.9 us                                                             | 27.7 us: 1.12x faster                                 |
| xml_etree_parse      | 162 ms                                                              | 156 ms: 1.04x faster                                  |
| xml_etree_iterparse  | 108 ms                                                              | 105 ms: 1.02x faster                                  |
| json_loads           | 26.2 us                                                             | 25.6 us: 1.02x faster                                 |
| json_dumps           | 12.5 ms                                                             | 12.6 ms: 1.01x slower                                 |
| pickle               | 9.79 us                                                             | 9.95 us: 1.02x slower                                 |
| unpickle_list        | 4.96 us                                                             | 5.21 us: 1.05x slower                                 |
| xml_etree_generate   | 76.5 ms                                                             | 80.8 ms: 1.06x slower                                 |
| xml_etree_process    | 54.1 ms                                                             | 57.8 ms: 1.07x slower                                 |
| unpickle_pure_python | 228 us                                                              | 251 us: 1.10x slower                                  |
| unpickle             | 13.2 us                                                             | 14.6 us: 1.10x slower                                 |
| pickle_pure_python   | 307 us                                                              | 347 us: 1.13x slower                                  |
| pickle_list          | 4.03 us                                                             | 4.68 us: 1.16x slower                                 |
| Geometric mean       | (ref)                                                               | 1.04x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.00 ms: 1.06x faster                                 |
| python_startup_no_site | 5.98 ms                                                             | 5.78 ms: 1.03x faster                                 |
| Geometric mean         | (ref)                                                               | 1.05x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 32.9 ms                                                             | 36.5 ms: 1.11x slower                                 |
| mako            | 9.82 ms                                                             | 11.9 ms: 1.21x slower                                 |
| Geometric mean  | (ref)                                                               | 1.16x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict             | 30.9 us                                                             | 27.7 us: 1.12x faster                                 |
| python_startup          | 8.49 ms                                                             | 8.00 ms: 1.06x faster                                 |
| xml_etree_parse         | 162 ms                                                              | 156 ms: 1.04x faster                                  |
| regex_effbot            | 3.32 ms                                                             | 3.21 ms: 1.03x faster                                 |
| python_startup_no_site  | 5.98 ms                                                             | 5.78 ms: 1.03x faster                                 |
| logging_format          | 6.64 us                                                             | 6.49 us: 1.02x faster                                 |
| xml_etree_iterparse     | 108 ms                                                              | 105 ms: 1.02x faster                                  |
| json_loads              | 26.2 us                                                             | 25.6 us: 1.02x faster                                 |
| logging_simple          | 6.09 us                                                             | 5.97 us: 1.02x faster                                 |
| meteor_contest          | 106 ms                                                              | 104 ms: 1.02x faster                                  |
| nbody                   | 96.7 ms                                                             | 96.1 ms: 1.01x faster                                 |
| unpack_sequence         | 49.5 ns                                                             | 49.2 ns: 1.01x faster                                 |
| json                    | 4.86 ms                                                             | 4.83 ms: 1.01x faster                                 |
| json_dumps              | 12.5 ms                                                             | 12.6 ms: 1.01x slower                                 |
| pidigits                | 197 ms                                                              | 198 ms: 1.01x slower                                  |
| fannkuch                | 384 ms                                                              | 386 ms: 1.01x slower                                  |
| nqueens                 | 84.0 ms                                                             | 84.6 ms: 1.01x slower                                 |
| scimark_fft             | 328 ms                                                              | 332 ms: 1.01x slower                                  |
| regex_compile           | 137 ms                                                              | 139 ms: 1.02x slower                                  |
| pickle                  | 9.79 us                                                             | 9.95 us: 1.02x slower                                 |
| 2to3                    | 257 ms                                                              | 264 ms: 1.03x slower                                  |
| sympy_sum               | 167 ms                                                              | 172 ms: 1.03x slower                                  |
| scimark_lu              | 108 ms                                                              | 112 ms: 1.03x slower                                  |
| sympy_integrate         | 21.0 ms                                                             | 21.7 ms: 1.03x slower                                 |
| spectral_norm           | 99.5 ms                                                             | 104 ms: 1.04x slower                                  |
| float                   | 76.0 ms                                                             | 79.2 ms: 1.04x slower                                 |
| hexiom                  | 6.48 ms                                                             | 6.77 ms: 1.04x slower                                 |
| unpickle_list           | 4.96 us                                                             | 5.21 us: 1.05x slower                                 |
| xml_etree_generate      | 76.5 ms                                                             | 80.8 ms: 1.06x slower                                 |
| dulwich_log             | 63.6 ms                                                             | 67.2 ms: 1.06x slower                                 |
| sympy_str               | 291 ms                                                              | 308 ms: 1.06x slower                                  |
| thrift                  | 766 us                                                              | 814 us: 1.06x slower                                  |
| pathlib                 | 18.2 ms                                                             | 19.4 ms: 1.07x slower                                 |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.77 ms: 1.07x slower                                 |
| sympy_expand            | 477 ms                                                              | 509 ms: 1.07x slower                                  |
| xml_etree_process       | 54.1 ms                                                             | 57.8 ms: 1.07x slower                                 |
| html5lib                | 64.0 ms                                                             | 68.5 ms: 1.07x slower                                 |
| regex_dna               | 196 ms                                                              | 212 ms: 1.08x slower                                  |
| pycparser               | 1.14 sec                                                            | 1.24 sec: 1.08x slower                                |
| chaos                   | 68.0 ms                                                             | 73.9 ms: 1.09x slower                                 |
| sqlite_synth            | 2.51 us                                                             | 2.74 us: 1.09x slower                                 |
| scimark_monte_carlo     | 67.8 ms                                                             | 74.0 ms: 1.09x slower                                 |
| unpickle_pure_python    | 228 us                                                              | 251 us: 1.10x slower                                  |
| unpickle                | 13.2 us                                                             | 14.6 us: 1.10x slower                                 |
| django_template         | 32.9 ms                                                             | 36.5 ms: 1.11x slower                                 |
| tornado_http            | 96.7 ms                                                             | 108 ms: 1.11x slower                                  |
| regex_v8                | 22.0 ms                                                             | 24.5 ms: 1.12x slower                                 |
| logging_silent          | 98.7 ns                                                             | 110 ns: 1.12x slower                                  |
| pickle_pure_python      | 307 us                                                              | 347 us: 1.13x slower                                  |
| scimark_sor             | 115 ms                                                              | 130 ms: 1.14x slower                                  |
| go                      | 138 ms                                                              | 158 ms: 1.14x slower                                  |
| raytrace                | 292 ms                                                              | 333 ms: 1.14x slower                                  |
| chameleon               | 6.52 ms                                                             | 7.44 ms: 1.14x slower                                 |
| pyflate                 | 414 ms                                                              | 477 ms: 1.15x slower                                  |
| pickle_list             | 4.03 us                                                             | 4.68 us: 1.16x slower                                 |
| richards                | 45.7 ms                                                             | 54.5 ms: 1.19x slower                                 |
| crypto_pyaes            | 73.8 ms                                                             | 88.1 ms: 1.19x slower                                 |
| mako                    | 9.82 ms                                                             | 11.9 ms: 1.21x slower                                 |
| deltablue               | 3.66 ms                                                             | 4.54 ms: 1.24x slower                                 |
| Geometric mean          | (ref)                                                               | 1.06x slower                                          |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
