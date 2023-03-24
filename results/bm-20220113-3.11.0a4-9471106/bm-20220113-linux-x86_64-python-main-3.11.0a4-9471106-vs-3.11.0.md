
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 9471106
- commit date: 2022-01-13
- overall geometric mean: 1.04x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 257 ms                                                              | 264 ms: 1.03x slower                                  |
| chameleon      | 6.52 ms                                                             | 7.55 ms: 1.16x slower                                 |
| html5lib       | 64.0 ms                                                             | 68.1 ms: 1.06x slower                                 |
| tornado_http   | 96.7 ms                                                             | 107 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                               | 1.09x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 95.1 ms: 1.02x faster                                 |
| pidigits       | 197 ms                                                              | 194 ms: 1.02x faster                                  |
| float          | 76.0 ms                                                             | 78.0 ms: 1.03x slower                                 |
| Geometric mean | (ref)                                                               | 1.00x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                             | 3.25 ms: 1.02x faster                                 |
| regex_compile  | 137 ms                                                              | 138 ms: 1.01x slower                                  |
| regex_dna      | 196 ms                                                              | 212 ms: 1.08x slower                                  |
| regex_v8       | 22.0 ms                                                             | 24.8 ms: 1.13x slower                                 |
| Geometric mean | (ref)                                                               | 1.05x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 30.9 us                                                             | 26.8 us: 1.15x faster                                 |
| xml_etree_parse      | 162 ms                                                              | 155 ms: 1.05x faster                                  |
| json_loads           | 26.2 us                                                             | 25.1 us: 1.04x faster                                 |
| json_dumps           | 12.5 ms                                                             | 12.4 ms: 1.01x faster                                 |
| pickle               | 9.79 us                                                             | 9.95 us: 1.02x slower                                 |
| xml_etree_generate   | 76.5 ms                                                             | 80.2 ms: 1.05x slower                                 |
| unpickle_list        | 4.96 us                                                             | 5.20 us: 1.05x slower                                 |
| xml_etree_process    | 54.1 ms                                                             | 56.9 ms: 1.05x slower                                 |
| pickle_pure_python   | 307 us                                                              | 329 us: 1.07x slower                                  |
| unpickle             | 13.2 us                                                             | 14.3 us: 1.08x slower                                 |
| pickle_list          | 4.03 us                                                             | 4.37 us: 1.08x slower                                 |
| unpickle_pure_python | 228 us                                                              | 254 us: 1.11x slower                                  |
| Geometric mean       | (ref)                                                               | 1.02x slower                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.07 ms: 1.05x faster                                 |
| python_startup_no_site | 5.98 ms                                                             | 5.85 ms: 1.02x faster                                 |
| Geometric mean         | (ref)                                                               | 1.04x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 32.9 ms                                                             | 35.2 ms: 1.07x slower                                 |
| mako            | 9.82 ms                                                             | 11.5 ms: 1.17x slower                                 |
| Geometric mean  | (ref)                                                               | 1.12x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict             | 30.9 us                                                             | 26.8 us: 1.15x faster                                 |
| unpack_sequence         | 49.5 ns                                                             | 44.8 ns: 1.10x faster                                 |
| python_startup          | 8.49 ms                                                             | 8.07 ms: 1.05x faster                                 |
| xml_etree_parse         | 162 ms                                                              | 155 ms: 1.05x faster                                  |
| json_loads              | 26.2 us                                                             | 25.1 us: 1.04x faster                                 |
| meteor_contest          | 106 ms                                                              | 103 ms: 1.03x faster                                  |
| logging_simple          | 6.09 us                                                             | 5.95 us: 1.02x faster                                 |
| json                    | 4.86 ms                                                             | 4.74 ms: 1.02x faster                                 |
| regex_effbot            | 3.32 ms                                                             | 3.25 ms: 1.02x faster                                 |
| python_startup_no_site  | 5.98 ms                                                             | 5.85 ms: 1.02x faster                                 |
| logging_format          | 6.64 us                                                             | 6.51 us: 1.02x faster                                 |
| nbody                   | 96.7 ms                                                             | 95.1 ms: 1.02x faster                                 |
| pidigits                | 197 ms                                                              | 194 ms: 1.02x faster                                  |
| json_dumps              | 12.5 ms                                                             | 12.4 ms: 1.01x faster                                 |
| sympy_sum               | 167 ms                                                              | 170 ms: 1.01x slower                                  |
| regex_compile           | 137 ms                                                              | 138 ms: 1.01x slower                                  |
| sympy_integrate         | 21.0 ms                                                             | 21.4 ms: 1.02x slower                                 |
| telco                   | 6.59 ms                                                             | 6.69 ms: 1.02x slower                                 |
| pickle                  | 9.79 us                                                             | 9.95 us: 1.02x slower                                 |
| pycparser               | 1.14 sec                                                            | 1.17 sec: 1.02x slower                                |
| fannkuch                | 384 ms                                                              | 392 ms: 1.02x slower                                  |
| hexiom                  | 6.48 ms                                                             | 6.63 ms: 1.02x slower                                 |
| 2to3                    | 257 ms                                                              | 264 ms: 1.03x slower                                  |
| float                   | 76.0 ms                                                             | 78.0 ms: 1.03x slower                                 |
| dulwich_log             | 63.6 ms                                                             | 65.8 ms: 1.03x slower                                 |
| sympy_str               | 291 ms                                                              | 302 ms: 1.03x slower                                  |
| xml_etree_generate      | 76.5 ms                                                             | 80.2 ms: 1.05x slower                                 |
| pathlib                 | 18.2 ms                                                             | 19.1 ms: 1.05x slower                                 |
| unpickle_list           | 4.96 us                                                             | 5.20 us: 1.05x slower                                 |
| scimark_lu              | 108 ms                                                              | 114 ms: 1.05x slower                                  |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.69 ms: 1.05x slower                                 |
| xml_etree_process       | 54.1 ms                                                             | 56.9 ms: 1.05x slower                                 |
| thrift                  | 766 us                                                              | 812 us: 1.06x slower                                  |
| sympy_expand            | 477 ms                                                              | 506 ms: 1.06x slower                                  |
| html5lib                | 64.0 ms                                                             | 68.1 ms: 1.06x slower                                 |
| chaos                   | 68.0 ms                                                             | 72.7 ms: 1.07x slower                                 |
| go                      | 138 ms                                                              | 148 ms: 1.07x slower                                  |
| django_template         | 32.9 ms                                                             | 35.2 ms: 1.07x slower                                 |
| scimark_monte_carlo     | 67.8 ms                                                             | 72.7 ms: 1.07x slower                                 |
| pyflate                 | 414 ms                                                              | 444 ms: 1.07x slower                                  |
| pickle_pure_python      | 307 us                                                              | 329 us: 1.07x slower                                  |
| regex_dna               | 196 ms                                                              | 212 ms: 1.08x slower                                  |
| unpickle                | 13.2 us                                                             | 14.3 us: 1.08x slower                                 |
| scimark_sor             | 115 ms                                                              | 124 ms: 1.08x slower                                  |
| pickle_list             | 4.03 us                                                             | 4.37 us: 1.08x slower                                 |
| sqlite_synth            | 2.51 us                                                             | 2.73 us: 1.09x slower                                 |
| raytrace                | 292 ms                                                              | 320 ms: 1.10x slower                                  |
| tornado_http            | 96.7 ms                                                             | 107 ms: 1.10x slower                                  |
| unpickle_pure_python    | 228 us                                                              | 254 us: 1.11x slower                                  |
| richards                | 45.7 ms                                                             | 51.5 ms: 1.13x slower                                 |
| regex_v8                | 22.0 ms                                                             | 24.8 ms: 1.13x slower                                 |
| crypto_pyaes            | 73.8 ms                                                             | 83.8 ms: 1.14x slower                                 |
| deltablue               | 3.66 ms                                                             | 4.16 ms: 1.14x slower                                 |
| logging_silent          | 98.7 ns                                                             | 113 ns: 1.15x slower                                  |
| chameleon               | 6.52 ms                                                             | 7.55 ms: 1.16x slower                                 |
| mako                    | 9.82 ms                                                             | 11.5 ms: 1.17x slower                                 |
| Geometric mean          | (ref)                                                               | 1.04x slower                                          |

Benchmark hidden because not significant (4): spectral_norm, xml_etree_iterparse, nqueens, scimark_fft
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
