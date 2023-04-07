
# Results vs. 3.11.0

- fork: iritkatriel
- ref: asyncgen
- machine: linux-x86_64
- commit hash: 4a2152f
- commit date: 2023-04-07
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 252 ms: 1.02x faster                                            |
| docutils       | 2.59 sec                                                            | 2.55 sec: 1.02x faster                                          |
| html5lib       | 64.0 ms                                                             | 62.0 ms: 1.03x faster                                           |
| tornado_http   | 96.7 ms                                                             | 90.9 ms: 1.06x faster                                           |
| Geometric mean | (ref)                                                               | 1.03x faster                                                    |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 87.4 ms: 1.11x faster                                           |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                            |
| float          | 76.0 ms                                                             | 74.4 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                               | 1.06x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 135 ms: 1.01x faster                                            |
| regex_v8       | 22.0 ms                                                             | 22.4 ms: 1.02x slower                                           |
| regex_dna      | 196 ms                                                              | 213 ms: 1.08x slower                                            |
| regex_effbot   | 3.32 ms                                                             | 3.74 ms: 1.12x slower                                           |
| Geometric mean | (ref)                                                               | 1.05x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.59 ms: 1.31x faster                                           |
| unpickle_pure_python | 228 us                                                              | 198 us: 1.15x faster                                            |
| xml_etree_parse      | 162 ms                                                              | 149 ms: 1.09x faster                                            |
| xml_etree_iterparse  | 108 ms                                                              | 99.4 ms: 1.08x faster                                           |
| json_loads           | 26.2 us                                                             | 24.3 us: 1.08x faster                                           |
| pickle_pure_python   | 307 us                                                              | 287 us: 1.07x faster                                            |
| xml_etree_process    | 54.1 ms                                                             | 55.0 ms: 1.02x slower                                           |
| unpickle             | 13.2 us                                                             | 13.4 us: 1.02x slower                                           |
| pickle_dict          | 30.9 us                                                             | 32.2 us: 1.04x slower                                           |
| xml_etree_generate   | 76.5 ms                                                             | 80.6 ms: 1.05x slower                                           |
| pickle_list          | 4.03 us                                                             | 4.24 us: 1.05x slower                                           |
| pickle               | 9.79 us                                                             | 10.4 us: 1.06x slower                                           |
| Geometric mean       | (ref)                                                               | 1.04x faster                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.84 ms: 1.04x slower                                           |
| python_startup_no_site | 5.98 ms                                                             | 6.52 ms: 1.09x slower                                           |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 47.8 ms: 1.08x faster                                           |
| genshi_text     | 21.8 ms                                                             | 21.6 ms: 1.01x faster                                           |
| django_template | 32.9 ms                                                             | 33.0 ms: 1.00x slower                                           |
| mako            | 9.82 ms                                                             | 9.97 ms: 1.02x slower                                           |
| Geometric mean  | (ref)                                                               | 1.02x faster                                                    |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 29.6 ms: 2.48x faster                                           |
| asyncio_tcp             | 888 ms                                                              | 507 ms: 1.75x faster                                            |
| json_dumps              | 12.5 ms                                                             | 9.59 ms: 1.31x faster                                           |
| mypy2                   | 422 ms                                                              | 332 ms: 1.27x faster                                            |
| unpack_sequence         | 49.5 ns                                                             | 42.7 ns: 1.16x faster                                           |
| unpickle_pure_python    | 228 us                                                              | 198 us: 1.15x faster                                            |
| deltablue               | 3.66 ms                                                             | 3.19 ms: 1.15x faster                                           |
| coroutines              | 26.3 ms                                                             | 23.3 ms: 1.13x faster                                           |
| nbody                   | 96.7 ms                                                             | 87.4 ms: 1.11x faster                                           |
| xml_etree_parse         | 162 ms                                                              | 149 ms: 1.09x faster                                            |
| xml_etree_iterparse     | 108 ms                                                              | 99.4 ms: 1.08x faster                                           |
| genshi_xml              | 51.8 ms                                                             | 47.8 ms: 1.08x faster                                           |
| json_loads              | 26.2 us                                                             | 24.3 us: 1.08x faster                                           |
| hexiom                  | 6.48 ms                                                             | 6.04 ms: 1.07x faster                                           |
| pickle_pure_python      | 307 us                                                              | 287 us: 1.07x faster                                            |
| deepcopy_memo           | 36.4 us                                                             | 34.0 us: 1.07x faster                                           |
| logging_simple          | 6.09 us                                                             | 5.70 us: 1.07x faster                                           |
| scimark_fft             | 328 ms                                                              | 307 ms: 1.07x faster                                            |
| tornado_http            | 96.7 ms                                                             | 90.9 ms: 1.06x faster                                           |
| logging_format          | 6.64 us                                                             | 6.25 us: 1.06x faster                                           |
| coverage                | 101 ms                                                              | 95.4 ms: 1.06x faster                                           |
| mdp                     | 2.64 sec                                                            | 2.50 sec: 1.06x faster                                          |
| deepcopy                | 339 us                                                              | 322 us: 1.05x faster                                            |
| nqueens                 | 84.0 ms                                                             | 80.1 ms: 1.05x faster                                           |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                            |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.05x faster                                           |
| logging_silent          | 98.7 ns                                                             | 94.5 ns: 1.05x faster                                           |
| raytrace                | 292 ms                                                              | 280 ms: 1.05x faster                                            |
| json                    | 4.86 ms                                                             | 4.65 ms: 1.04x faster                                           |
| sqlglot_optimize        | 53.4 ms                                                             | 51.2 ms: 1.04x faster                                           |
| gunicorn                | 1.13 ms                                                             | 1.09 ms: 1.04x faster                                           |
| sympy_expand            | 477 ms                                                              | 460 ms: 1.04x faster                                            |
| bench_thread_pool       | 820 us                                                              | 790 us: 1.04x faster                                            |
| scimark_sor             | 115 ms                                                              | 111 ms: 1.04x faster                                            |
| meteor_contest          | 106 ms                                                              | 103 ms: 1.04x faster                                            |
| spectral_norm           | 99.5 ms                                                             | 96.2 ms: 1.03x faster                                           |
| sympy_integrate         | 21.0 ms                                                             | 20.4 ms: 1.03x faster                                           |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.33 ms: 1.03x faster                                           |
| html5lib                | 64.0 ms                                                             | 62.0 ms: 1.03x faster                                           |
| richards                | 45.7 ms                                                             | 44.3 ms: 1.03x faster                                           |
| sqlglot_normalize       | 108 ms                                                              | 105 ms: 1.03x faster                                            |
| pprint_pformat          | 1.45 sec                                                            | 1.41 sec: 1.03x faster                                          |
| sympy_str               | 291 ms                                                              | 284 ms: 1.03x faster                                            |
| chaos                   | 68.0 ms                                                             | 66.3 ms: 1.03x faster                                           |
| float                   | 76.0 ms                                                             | 74.4 ms: 1.02x faster                                           |
| 2to3                    | 257 ms                                                              | 252 ms: 1.02x faster                                            |
| pprint_safe_repr        | 701 ms                                                              | 687 ms: 1.02x faster                                            |
| deepcopy_reduce         | 2.96 us                                                             | 2.90 us: 1.02x faster                                           |
| telco                   | 6.59 ms                                                             | 6.46 ms: 1.02x faster                                           |
| sqlalchemy_imperative   | 18.0 ms                                                             | 17.7 ms: 1.02x faster                                           |
| docutils                | 2.59 sec                                                            | 2.55 sec: 1.02x faster                                          |
| sqlalchemy_declarative  | 138 ms                                                              | 136 ms: 1.02x faster                                            |
| regex_compile           | 137 ms                                                              | 135 ms: 1.01x faster                                            |
| genshi_text             | 21.8 ms                                                             | 21.6 ms: 1.01x faster                                           |
| dulwich_log             | 63.6 ms                                                             | 63.0 ms: 1.01x faster                                           |
| create_gc_cycles        | 1.48 ms                                                             | 1.47 ms: 1.01x faster                                           |
| pathlib                 | 18.2 ms                                                             | 18.1 ms: 1.01x faster                                           |
| sympy_sum               | 167 ms                                                              | 166 ms: 1.01x faster                                            |
| django_template         | 32.9 ms                                                             | 33.0 ms: 1.00x slower                                           |
| go                      | 138 ms                                                              | 140 ms: 1.01x slower                                            |
| async_tree_io           | 1.28 sec                                                            | 1.30 sec: 1.01x slower                                          |
| mako                    | 9.82 ms                                                             | 9.97 ms: 1.02x slower                                           |
| xml_etree_process       | 54.1 ms                                                             | 55.0 ms: 1.02x slower                                           |
| scimark_monte_carlo     | 67.8 ms                                                             | 68.9 ms: 1.02x slower                                           |
| unpickle                | 13.2 us                                                             | 13.4 us: 1.02x slower                                           |
| pyflate                 | 414 ms                                                              | 421 ms: 1.02x slower                                            |
| thrift                  | 766 us                                                              | 781 us: 1.02x slower                                            |
| regex_v8                | 22.0 ms                                                             | 22.4 ms: 1.02x slower                                           |
| async_tree_memoization  | 621 ms                                                              | 637 ms: 1.03x slower                                            |
| fannkuch                | 384 ms                                                              | 394 ms: 1.03x slower                                            |
| sqlite_synth            | 2.51 us                                                             | 2.61 us: 1.04x slower                                           |
| pickle_dict             | 30.9 us                                                             | 32.2 us: 1.04x slower                                           |
| sqlglot_transpile       | 1.65 ms                                                             | 1.72 ms: 1.04x slower                                           |
| python_startup          | 8.49 ms                                                             | 8.84 ms: 1.04x slower                                           |
| sqlglot_parse           | 1.36 ms                                                             | 1.43 ms: 1.05x slower                                           |
| xml_etree_generate      | 76.5 ms                                                             | 80.6 ms: 1.05x slower                                           |
| pickle_list             | 4.03 us                                                             | 4.24 us: 1.05x slower                                           |
| pickle                  | 9.79 us                                                             | 10.4 us: 1.06x slower                                           |
| comprehensions          | 22.2 us                                                             | 23.8 us: 1.07x slower                                           |
| regex_dna               | 196 ms                                                              | 213 ms: 1.08x slower                                            |
| python_startup_no_site  | 5.98 ms                                                             | 6.52 ms: 1.09x slower                                           |
| regex_effbot            | 3.32 ms                                                             | 3.74 ms: 1.12x slower                                           |
| async_generators        | 361 ms                                                              | 407 ms: 1.13x slower                                            |
| gc_traversal            | 3.63 ms                                                             | 4.32 ms: 1.19x slower                                           |
| dask                    | 368 ms                                                              | 509 ms: 1.38x slower                                            |
| Geometric mean          | (ref)                                                               | 1.03x faster                                                    |

Benchmark hidden because not significant (9): async_tree_none, pycparser, bench_mp_pool, scimark_lu, chameleon, unpickle_list, crypto_pyaes, async_tree_cpu_io_mixed, djangocms
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
