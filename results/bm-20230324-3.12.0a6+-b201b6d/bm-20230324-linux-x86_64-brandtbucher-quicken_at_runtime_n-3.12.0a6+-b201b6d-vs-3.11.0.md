
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime_n
- machine: linux-x86_64
- commit hash: b201b6d
- commit date: 2023-03-24
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 253 ms: 1.02x faster                                                         |
| docutils       | 2.59 sec                                                            | 2.54 sec: 1.02x faster                                                       |
| html5lib       | 64.0 ms                                                             | 62.6 ms: 1.02x faster                                                        |
| tornado_http   | 96.7 ms                                                             | 91.6 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                               | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 88.6 ms: 1.09x faster                                                        |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                         |
| float          | 76.0 ms                                                             | 74.4 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                               | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 21.3 ms: 1.03x faster                                                        |
| regex_compile  | 137 ms                                                              | 136 ms: 1.01x faster                                                         |
| regex_dna      | 196 ms                                                              | 202 ms: 1.03x slower                                                         |
| regex_effbot   | 3.32 ms                                                             | 3.41 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.73 ms: 1.29x faster                                                        |
| unpickle_pure_python | 228 us                                                              | 202 us: 1.13x faster                                                         |
| xml_etree_parse      | 162 ms                                                              | 148 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 108 ms                                                              | 99.9 ms: 1.08x faster                                                        |
| json_loads           | 26.2 us                                                             | 24.5 us: 1.07x faster                                                        |
| pickle_pure_python   | 307 us                                                              | 294 us: 1.04x faster                                                         |
| unpickle_list        | 4.96 us                                                             | 4.92 us: 1.01x faster                                                        |
| pickle_dict          | 30.9 us                                                             | 31.7 us: 1.02x slower                                                        |
| pickle_list          | 4.03 us                                                             | 4.20 us: 1.04x slower                                                        |
| xml_etree_process    | 54.1 ms                                                             | 56.5 ms: 1.04x slower                                                        |
| unpickle             | 13.2 us                                                             | 13.9 us: 1.05x slower                                                        |
| xml_etree_generate   | 76.5 ms                                                             | 81.1 ms: 1.06x slower                                                        |
| pickle               | 9.79 us                                                             | 10.5 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.65 ms: 1.02x slower                                                        |
| python_startup_no_site | 5.98 ms                                                             | 6.34 ms: 1.06x slower                                                        |
| Geometric mean         | (ref)                                                               | 1.04x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 48.5 ms: 1.07x faster                                                        |
| genshi_text     | 21.8 ms                                                             | 22.5 ms: 1.03x slower                                                        |
| django_template | 32.9 ms                                                             | 33.9 ms: 1.03x slower                                                        |
| mako            | 9.82 ms                                                             | 10.1 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                               | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 29.1 ms: 2.52x faster                                                        |
| asyncio_tcp             | 888 ms                                                              | 509 ms: 1.74x faster                                                         |
| json_dumps              | 12.5 ms                                                             | 9.73 ms: 1.29x faster                                                        |
| mypy2                   | 422 ms                                                              | 335 ms: 1.26x faster                                                         |
| unpickle_pure_python    | 228 us                                                              | 202 us: 1.13x faster                                                         |
| deltablue               | 3.66 ms                                                             | 3.26 ms: 1.12x faster                                                        |
| unpack_sequence         | 49.5 ns                                                             | 44.4 ns: 1.11x faster                                                        |
| xml_etree_parse         | 162 ms                                                              | 148 ms: 1.09x faster                                                         |
| spectral_norm           | 99.5 ms                                                             | 91.1 ms: 1.09x faster                                                        |
| nbody                   | 96.7 ms                                                             | 88.6 ms: 1.09x faster                                                        |
| coroutines              | 26.3 ms                                                             | 24.1 ms: 1.09x faster                                                        |
| xml_etree_iterparse     | 108 ms                                                              | 99.9 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.17 ms: 1.07x faster                                                        |
| hexiom                  | 6.48 ms                                                             | 6.06 ms: 1.07x faster                                                        |
| genshi_xml              | 51.8 ms                                                             | 48.5 ms: 1.07x faster                                                        |
| json_loads              | 26.2 us                                                             | 24.5 us: 1.07x faster                                                        |
| scimark_fft             | 328 ms                                                              | 308 ms: 1.06x faster                                                         |
| deepcopy_memo           | 36.4 us                                                             | 34.4 us: 1.06x faster                                                        |
| tornado_http            | 96.7 ms                                                             | 91.6 ms: 1.06x faster                                                        |
| coverage                | 101 ms                                                              | 96.3 ms: 1.05x faster                                                        |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                         |
| json                    | 4.86 ms                                                             | 4.65 ms: 1.04x faster                                                        |
| pickle_pure_python      | 307 us                                                              | 294 us: 1.04x faster                                                         |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.04x faster                                                        |
| nqueens                 | 84.0 ms                                                             | 80.6 ms: 1.04x faster                                                        |
| richards                | 45.7 ms                                                             | 44.2 ms: 1.03x faster                                                        |
| sqlglot_optimize        | 53.4 ms                                                             | 51.6 ms: 1.03x faster                                                        |
| mdp                     | 2.64 sec                                                            | 2.55 sec: 1.03x faster                                                       |
| gunicorn                | 1.13 ms                                                             | 1.09 ms: 1.03x faster                                                        |
| regex_v8                | 22.0 ms                                                             | 21.3 ms: 1.03x faster                                                        |
| bench_thread_pool       | 820 us                                                              | 794 us: 1.03x faster                                                         |
| scimark_sor             | 115 ms                                                              | 111 ms: 1.03x faster                                                         |
| raytrace                | 292 ms                                                              | 284 ms: 1.03x faster                                                         |
| pycparser               | 1.14 sec                                                            | 1.12 sec: 1.03x faster                                                       |
| meteor_contest          | 106 ms                                                              | 104 ms: 1.02x faster                                                         |
| logging_silent          | 98.7 ns                                                             | 96.5 ns: 1.02x faster                                                        |
| html5lib                | 64.0 ms                                                             | 62.6 ms: 1.02x faster                                                        |
| sympy_expand            | 477 ms                                                              | 467 ms: 1.02x faster                                                         |
| float                   | 76.0 ms                                                             | 74.4 ms: 1.02x faster                                                        |
| docutils                | 2.59 sec                                                            | 2.54 sec: 1.02x faster                                                       |
| pprint_pformat          | 1.45 sec                                                            | 1.42 sec: 1.02x faster                                                       |
| 2to3                    | 257 ms                                                              | 253 ms: 1.02x faster                                                         |
| telco                   | 6.59 ms                                                             | 6.48 ms: 1.02x faster                                                        |
| deepcopy                | 339 us                                                              | 333 us: 1.02x faster                                                         |
| chaos                   | 68.0 ms                                                             | 66.9 ms: 1.02x faster                                                        |
| sympy_integrate         | 21.0 ms                                                             | 20.8 ms: 1.01x faster                                                        |
| sympy_str               | 291 ms                                                              | 288 ms: 1.01x faster                                                         |
| sqlalchemy_declarative  | 138 ms                                                              | 137 ms: 1.01x faster                                                         |
| unpickle_list           | 4.96 us                                                             | 4.92 us: 1.01x faster                                                        |
| logging_format          | 6.64 us                                                             | 6.58 us: 1.01x faster                                                        |
| regex_compile           | 137 ms                                                              | 136 ms: 1.01x faster                                                         |
| sqlglot_normalize       | 108 ms                                                              | 108 ms: 1.01x faster                                                         |
| logging_simple          | 6.09 us                                                             | 6.05 us: 1.01x faster                                                        |
| create_gc_cycles        | 1.48 ms                                                             | 1.48 ms: 1.00x slower                                                        |
| sympy_sum               | 167 ms                                                              | 168 ms: 1.00x slower                                                         |
| async_tree_io           | 1.28 sec                                                            | 1.30 sec: 1.02x slower                                                       |
| go                      | 138 ms                                                              | 141 ms: 1.02x slower                                                         |
| python_startup          | 8.49 ms                                                             | 8.65 ms: 1.02x slower                                                        |
| pickle_dict             | 30.9 us                                                             | 31.7 us: 1.02x slower                                                        |
| regex_dna               | 196 ms                                                              | 202 ms: 1.03x slower                                                         |
| deepcopy_reduce         | 2.96 us                                                             | 3.04 us: 1.03x slower                                                        |
| regex_effbot            | 3.32 ms                                                             | 3.41 ms: 1.03x slower                                                        |
| genshi_text             | 21.8 ms                                                             | 22.5 ms: 1.03x slower                                                        |
| django_template         | 32.9 ms                                                             | 33.9 ms: 1.03x slower                                                        |
| mako                    | 9.82 ms                                                             | 10.1 ms: 1.03x slower                                                        |
| pyflate                 | 414 ms                                                              | 427 ms: 1.03x slower                                                         |
| sqlite_synth            | 2.51 us                                                             | 2.60 us: 1.04x slower                                                        |
| thrift                  | 766 us                                                              | 795 us: 1.04x slower                                                         |
| pickle_list             | 4.03 us                                                             | 4.20 us: 1.04x slower                                                        |
| xml_etree_process       | 54.1 ms                                                             | 56.5 ms: 1.04x slower                                                        |
| async_tree_memoization  | 621 ms                                                              | 651 ms: 1.05x slower                                                         |
| sqlglot_transpile       | 1.65 ms                                                             | 1.73 ms: 1.05x slower                                                        |
| unpickle                | 13.2 us                                                             | 13.9 us: 1.05x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                             | 1.44 ms: 1.06x slower                                                        |
| xml_etree_generate      | 76.5 ms                                                             | 81.1 ms: 1.06x slower                                                        |
| python_startup_no_site  | 5.98 ms                                                             | 6.34 ms: 1.06x slower                                                        |
| comprehensions          | 22.2 us                                                             | 23.7 us: 1.06x slower                                                        |
| pickle                  | 9.79 us                                                             | 10.5 us: 1.08x slower                                                        |
| gc_traversal            | 3.63 ms                                                             | 3.93 ms: 1.08x slower                                                        |
| async_generators        | 361 ms                                                              | 409 ms: 1.13x slower                                                         |
| dask                    | 368 ms                                                              | 515 ms: 1.40x slower                                                         |
| Geometric mean          | (ref)                                                               | 1.03x faster                                                                 |

Benchmark hidden because not significant (13): scimark_monte_carlo, chameleon, pprint_safe_repr, bench_mp_pool, pathlib, dulwich_log, crypto_pyaes, fannkuch, async_tree_none, scimark_lu, sqlalchemy_imperative, djangocms, async_tree_cpu_io_mixed
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
