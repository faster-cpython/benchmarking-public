
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_call_more
- machine: linux-x86_64
- commit hash: d02b607
- commit date: 2023-04-04
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 251 ms: 1.02x faster                                                     |
| chameleon      | 6.52 ms                                                             | 6.67 ms: 1.02x slower                                                    |
| docutils       | 2.59 sec                                                            | 2.54 sec: 1.02x faster                                                   |
| html5lib       | 64.0 ms                                                             | 60.8 ms: 1.05x faster                                                    |
| tornado_http   | 96.7 ms                                                             | 90.8 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                               | 1.03x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 88.1 ms: 1.10x faster                                                    |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                     |
| float          | 76.0 ms                                                             | 74.1 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                               | 1.06x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 132 ms: 1.03x faster                                                     |
| regex_v8       | 22.0 ms                                                             | 21.7 ms: 1.01x faster                                                    |
| regex_dna      | 196 ms                                                              | 205 ms: 1.04x slower                                                     |
| regex_effbot   | 3.32 ms                                                             | 3.69 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                               | 1.03x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.49 ms: 1.32x faster                                                    |
| unpickle_pure_python | 228 us                                                              | 199 us: 1.15x faster                                                     |
| xml_etree_parse      | 162 ms                                                              | 148 ms: 1.10x faster                                                     |
| pickle_pure_python   | 307 us                                                              | 284 us: 1.08x faster                                                     |
| xml_etree_iterparse  | 108 ms                                                              | 99.9 ms: 1.08x faster                                                    |
| json_loads           | 26.2 us                                                             | 24.3 us: 1.08x faster                                                    |
| pickle_dict          | 30.9 us                                                             | 31.4 us: 1.02x slower                                                    |
| xml_etree_process    | 54.1 ms                                                             | 56.4 ms: 1.04x slower                                                    |
| unpickle_list        | 4.96 us                                                             | 5.17 us: 1.04x slower                                                    |
| pickle               | 9.79 us                                                             | 10.5 us: 1.07x slower                                                    |
| xml_etree_generate   | 76.5 ms                                                             | 82.1 ms: 1.07x slower                                                    |
| pickle_list          | 4.03 us                                                             | 4.36 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.78 ms: 1.03x slower                                                    |
| python_startup_no_site | 5.98 ms                                                             | 6.49 ms: 1.09x slower                                                    |
| Geometric mean         | (ref)                                                               | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 48.0 ms: 1.08x faster                                                    |
| genshi_text     | 21.8 ms                                                             | 21.2 ms: 1.03x faster                                                    |
| django_template | 32.9 ms                                                             | 33.8 ms: 1.03x slower                                                    |
| mako            | 9.82 ms                                                             | 10.2 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                               | 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 29.3 ms: 2.51x faster                                                    |
| asyncio_tcp             | 888 ms                                                              | 500 ms: 1.77x faster                                                     |
| json_dumps              | 12.5 ms                                                             | 9.49 ms: 1.32x faster                                                    |
| mypy2                   | 422 ms                                                              | 331 ms: 1.27x faster                                                     |
| unpack_sequence         | 49.5 ns                                                             | 42.4 ns: 1.17x faster                                                    |
| unpickle_pure_python    | 228 us                                                              | 199 us: 1.15x faster                                                     |
| deltablue               | 3.66 ms                                                             | 3.25 ms: 1.13x faster                                                    |
| coroutines              | 26.3 ms                                                             | 23.5 ms: 1.12x faster                                                    |
| nbody                   | 96.7 ms                                                             | 88.1 ms: 1.10x faster                                                    |
| xml_etree_parse         | 162 ms                                                              | 148 ms: 1.10x faster                                                     |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.13 ms: 1.08x faster                                                    |
| pickle_pure_python      | 307 us                                                              | 284 us: 1.08x faster                                                     |
| genshi_xml              | 51.8 ms                                                             | 48.0 ms: 1.08x faster                                                    |
| xml_etree_iterparse     | 108 ms                                                              | 99.9 ms: 1.08x faster                                                    |
| json_loads              | 26.2 us                                                             | 24.3 us: 1.08x faster                                                    |
| tornado_http            | 96.7 ms                                                             | 90.8 ms: 1.06x faster                                                    |
| scimark_fft             | 328 ms                                                              | 309 ms: 1.06x faster                                                     |
| deepcopy_memo           | 36.4 us                                                             | 34.4 us: 1.06x faster                                                    |
| logging_simple          | 6.09 us                                                             | 5.76 us: 1.06x faster                                                    |
| json                    | 4.86 ms                                                             | 4.61 ms: 1.05x faster                                                    |
| spectral_norm           | 99.5 ms                                                             | 94.5 ms: 1.05x faster                                                    |
| html5lib                | 64.0 ms                                                             | 60.8 ms: 1.05x faster                                                    |
| coverage                | 101 ms                                                              | 96.1 ms: 1.05x faster                                                    |
| hexiom                  | 6.48 ms                                                             | 6.16 ms: 1.05x faster                                                    |
| richards                | 45.7 ms                                                             | 43.5 ms: 1.05x faster                                                    |
| logging_format          | 6.64 us                                                             | 6.34 us: 1.05x faster                                                    |
| raytrace                | 292 ms                                                              | 279 ms: 1.05x faster                                                     |
| pycparser               | 1.14 sec                                                            | 1.09 sec: 1.05x faster                                                   |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.05x faster                                                    |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                     |
| gunicorn                | 1.13 ms                                                             | 1.08 ms: 1.04x faster                                                    |
| bench_thread_pool       | 820 us                                                              | 790 us: 1.04x faster                                                     |
| sqlglot_optimize        | 53.4 ms                                                             | 51.6 ms: 1.03x faster                                                    |
| mdp                     | 2.64 sec                                                            | 2.55 sec: 1.03x faster                                                   |
| chaos                   | 68.0 ms                                                             | 65.8 ms: 1.03x faster                                                    |
| regex_compile           | 137 ms                                                              | 132 ms: 1.03x faster                                                     |
| genshi_text             | 21.8 ms                                                             | 21.2 ms: 1.03x faster                                                    |
| sympy_integrate         | 21.0 ms                                                             | 20.5 ms: 1.03x faster                                                    |
| sympy_expand            | 477 ms                                                              | 464 ms: 1.03x faster                                                     |
| sqlglot_normalize       | 108 ms                                                              | 105 ms: 1.03x faster                                                     |
| float                   | 76.0 ms                                                             | 74.1 ms: 1.03x faster                                                    |
| sympy_str               | 291 ms                                                              | 284 ms: 1.02x faster                                                     |
| 2to3                    | 257 ms                                                              | 251 ms: 1.02x faster                                                     |
| sqlalchemy_declarative  | 138 ms                                                              | 136 ms: 1.02x faster                                                     |
| docutils                | 2.59 sec                                                            | 2.54 sec: 1.02x faster                                                   |
| meteor_contest          | 106 ms                                                              | 104 ms: 1.02x faster                                                     |
| deepcopy                | 339 us                                                              | 333 us: 1.02x faster                                                     |
| sqlalchemy_imperative   | 18.0 ms                                                             | 17.7 ms: 1.02x faster                                                    |
| nqueens                 | 84.0 ms                                                             | 82.7 ms: 1.02x faster                                                    |
| pprint_pformat          | 1.45 sec                                                            | 1.43 sec: 1.01x faster                                                   |
| regex_v8                | 22.0 ms                                                             | 21.7 ms: 1.01x faster                                                    |
| pathlib                 | 18.2 ms                                                             | 18.0 ms: 1.01x faster                                                    |
| go                      | 138 ms                                                              | 137 ms: 1.01x faster                                                     |
| pprint_safe_repr        | 701 ms                                                              | 695 ms: 1.01x faster                                                     |
| sympy_sum               | 167 ms                                                              | 166 ms: 1.01x faster                                                     |
| logging_silent          | 98.7 ns                                                             | 98.3 ns: 1.00x faster                                                    |
| async_tree_io           | 1.28 sec                                                            | 1.29 sec: 1.01x slower                                                   |
| deepcopy_reduce         | 2.96 us                                                             | 2.99 us: 1.01x slower                                                    |
| scimark_monte_carlo     | 67.8 ms                                                             | 68.6 ms: 1.01x slower                                                    |
| fannkuch                | 384 ms                                                              | 388 ms: 1.01x slower                                                     |
| scimark_sor             | 115 ms                                                              | 116 ms: 1.01x slower                                                     |
| pickle_dict             | 30.9 us                                                             | 31.4 us: 1.02x slower                                                    |
| crypto_pyaes            | 73.8 ms                                                             | 75.3 ms: 1.02x slower                                                    |
| async_tree_memoization  | 621 ms                                                              | 635 ms: 1.02x slower                                                     |
| thrift                  | 766 us                                                              | 783 us: 1.02x slower                                                     |
| chameleon               | 6.52 ms                                                             | 6.67 ms: 1.02x slower                                                    |
| django_template         | 32.9 ms                                                             | 33.8 ms: 1.03x slower                                                    |
| mako                    | 9.82 ms                                                             | 10.2 ms: 1.03x slower                                                    |
| python_startup          | 8.49 ms                                                             | 8.78 ms: 1.03x slower                                                    |
| xml_etree_process       | 54.1 ms                                                             | 56.4 ms: 1.04x slower                                                    |
| unpickle_list           | 4.96 us                                                             | 5.17 us: 1.04x slower                                                    |
| regex_dna               | 196 ms                                                              | 205 ms: 1.04x slower                                                     |
| sqlite_synth            | 2.51 us                                                             | 2.66 us: 1.06x slower                                                    |
| sqlglot_transpile       | 1.65 ms                                                             | 1.75 ms: 1.06x slower                                                    |
| pyflate                 | 414 ms                                                              | 441 ms: 1.07x slower                                                     |
| sqlglot_parse           | 1.36 ms                                                             | 1.45 ms: 1.07x slower                                                    |
| comprehensions          | 22.2 us                                                             | 23.8 us: 1.07x slower                                                    |
| pickle                  | 9.79 us                                                             | 10.5 us: 1.07x slower                                                    |
| xml_etree_generate      | 76.5 ms                                                             | 82.1 ms: 1.07x slower                                                    |
| pickle_list             | 4.03 us                                                             | 4.36 us: 1.08x slower                                                    |
| python_startup_no_site  | 5.98 ms                                                             | 6.49 ms: 1.09x slower                                                    |
| regex_effbot            | 3.32 ms                                                             | 3.69 ms: 1.11x slower                                                    |
| async_generators        | 361 ms                                                              | 417 ms: 1.15x slower                                                     |
| gc_traversal            | 3.63 ms                                                             | 4.32 ms: 1.19x slower                                                    |
| dask                    | 368 ms                                                              | 510 ms: 1.39x slower                                                     |
| Geometric mean          | (ref)                                                               | 1.03x faster                                                             |

Benchmark hidden because not significant (9): async_tree_none, djangocms, scimark_lu, telco, async_tree_cpu_io_mixed, create_gc_cycles, bench_mp_pool, dulwich_log, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
