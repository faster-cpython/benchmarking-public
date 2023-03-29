
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_call
- machine: linux-x86_64
- commit hash: 187f060
- commit date: 2023-03-25
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 251 ms: 1.02x faster                                                |
| chameleon      | 6.52 ms                                                             | 6.48 ms: 1.01x faster                                               |
| docutils       | 2.59 sec                                                            | 2.56 sec: 1.01x faster                                              |
| html5lib       | 64.0 ms                                                             | 61.2 ms: 1.05x faster                                               |
| tornado_http   | 96.7 ms                                                             | 91.6 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                               | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 88.2 ms: 1.10x faster                                               |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                |
| float          | 76.0 ms                                                             | 74.4 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                               | 1.05x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 135 ms: 1.01x faster                                                |
| regex_v8       | 22.0 ms                                                             | 21.8 ms: 1.01x faster                                               |
| regex_dna      | 196 ms                                                              | 204 ms: 1.04x slower                                                |
| regex_effbot   | 3.32 ms                                                             | 3.64 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                               | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.62 ms: 1.30x faster                                               |
| unpickle_pure_python | 228 us                                                              | 202 us: 1.13x faster                                                |
| xml_etree_parse      | 162 ms                                                              | 149 ms: 1.09x faster                                                |
| json_loads           | 26.2 us                                                             | 24.3 us: 1.08x faster                                               |
| pickle_pure_python   | 307 us                                                              | 289 us: 1.06x faster                                                |
| xml_etree_iterparse  | 108 ms                                                              | 103 ms: 1.04x faster                                                |
| pickle_dict          | 30.9 us                                                             | 31.5 us: 1.02x slower                                               |
| xml_etree_process    | 54.1 ms                                                             | 55.3 ms: 1.02x slower                                               |
| unpickle_list        | 4.96 us                                                             | 5.17 us: 1.04x slower                                               |
| pickle_list          | 4.03 us                                                             | 4.21 us: 1.04x slower                                               |
| xml_etree_generate   | 76.5 ms                                                             | 80.2 ms: 1.05x slower                                               |
| unpickle             | 13.2 us                                                             | 13.9 us: 1.05x slower                                               |
| pickle               | 9.79 us                                                             | 10.3 us: 1.05x slower                                               |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.83 ms: 1.04x slower                                               |
| python_startup_no_site | 5.98 ms                                                             | 6.53 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                             | 48.6 ms: 1.07x faster                                               |
| genshi_text    | 21.8 ms                                                             | 21.7 ms: 1.01x faster                                               |
| mako           | 9.82 ms                                                             | 10.0 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                               | 1.01x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-187f060 |
|-------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 28.7 ms: 2.56x faster                                               |
| asyncio_tcp             | 888 ms                                                              | 505 ms: 1.76x faster                                                |
| json_dumps              | 12.5 ms                                                             | 9.62 ms: 1.30x faster                                               |
| mypy2                   | 422 ms                                                              | 332 ms: 1.27x faster                                                |
| coroutines              | 26.3 ms                                                             | 22.7 ms: 1.16x faster                                               |
| deltablue               | 3.66 ms                                                             | 3.23 ms: 1.13x faster                                               |
| unpickle_pure_python    | 228 us                                                              | 202 us: 1.13x faster                                                |
| unpack_sequence         | 49.5 ns                                                             | 44.0 ns: 1.12x faster                                               |
| nbody                   | 96.7 ms                                                             | 88.2 ms: 1.10x faster                                               |
| xml_etree_parse         | 162 ms                                                              | 149 ms: 1.09x faster                                                |
| scimark_fft             | 328 ms                                                              | 304 ms: 1.08x faster                                                |
| json_loads              | 26.2 us                                                             | 24.3 us: 1.08x faster                                               |
| logging_simple          | 6.09 us                                                             | 5.68 us: 1.07x faster                                               |
| hexiom                  | 6.48 ms                                                             | 6.05 ms: 1.07x faster                                               |
| deepcopy_memo           | 36.4 us                                                             | 34.1 us: 1.07x faster                                               |
| genshi_xml              | 51.8 ms                                                             | 48.6 ms: 1.07x faster                                               |
| logging_format          | 6.64 us                                                             | 6.23 us: 1.06x faster                                               |
| pickle_pure_python      | 307 us                                                              | 289 us: 1.06x faster                                                |
| tornado_http            | 96.7 ms                                                             | 91.6 ms: 1.06x faster                                               |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.24 ms: 1.05x faster                                               |
| richards                | 45.7 ms                                                             | 43.4 ms: 1.05x faster                                               |
| coverage                | 101 ms                                                              | 96.1 ms: 1.05x faster                                               |
| raytrace                | 292 ms                                                              | 278 ms: 1.05x faster                                                |
| spectral_norm           | 99.5 ms                                                             | 94.7 ms: 1.05x faster                                               |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.05x faster                                               |
| html5lib                | 64.0 ms                                                             | 61.2 ms: 1.05x faster                                               |
| xml_etree_iterparse     | 108 ms                                                              | 103 ms: 1.04x faster                                                |
| logging_silent          | 98.7 ns                                                             | 94.8 ns: 1.04x faster                                               |
| json                    | 4.86 ms                                                             | 4.67 ms: 1.04x faster                                               |
| sqlglot_optimize        | 53.4 ms                                                             | 51.4 ms: 1.04x faster                                               |
| bench_thread_pool       | 820 us                                                              | 791 us: 1.04x faster                                                |
| sqlglot_normalize       | 108 ms                                                              | 105 ms: 1.04x faster                                                |
| sympy_expand            | 477 ms                                                              | 461 ms: 1.03x faster                                                |
| pycparser               | 1.14 sec                                                            | 1.11 sec: 1.03x faster                                              |
| fannkuch                | 384 ms                                                              | 371 ms: 1.03x faster                                                |
| gunicorn                | 1.13 ms                                                             | 1.09 ms: 1.03x faster                                               |
| sympy_str               | 291 ms                                                              | 282 ms: 1.03x faster                                                |
| scimark_sor             | 115 ms                                                              | 111 ms: 1.03x faster                                                |
| pathlib                 | 18.2 ms                                                             | 17.7 ms: 1.03x faster                                               |
| sqlalchemy_imperative   | 18.0 ms                                                             | 17.5 ms: 1.03x faster                                               |
| sympy_integrate         | 21.0 ms                                                             | 20.5 ms: 1.03x faster                                               |
| chaos                   | 68.0 ms                                                             | 66.0 ms: 1.03x faster                                               |
| deepcopy                | 339 us                                                              | 331 us: 1.02x faster                                                |
| gc_traversal            | 3.63 ms                                                             | 3.54 ms: 1.02x faster                                               |
| 2to3                    | 257 ms                                                              | 251 ms: 1.02x faster                                                |
| meteor_contest          | 106 ms                                                              | 104 ms: 1.02x faster                                                |
| float                   | 76.0 ms                                                             | 74.4 ms: 1.02x faster                                               |
| nqueens                 | 84.0 ms                                                             | 82.3 ms: 1.02x faster                                               |
| pprint_pformat          | 1.45 sec                                                            | 1.43 sec: 1.02x faster                                              |
| deepcopy_reduce         | 2.96 us                                                             | 2.91 us: 1.02x faster                                               |
| sqlalchemy_declarative  | 138 ms                                                              | 136 ms: 1.02x faster                                                |
| regex_compile           | 137 ms                                                              | 135 ms: 1.01x faster                                                |
| docutils                | 2.59 sec                                                            | 2.56 sec: 1.01x faster                                              |
| sympy_sum               | 167 ms                                                              | 166 ms: 1.01x faster                                                |
| telco                   | 6.59 ms                                                             | 6.54 ms: 1.01x faster                                               |
| pprint_safe_repr        | 701 ms                                                              | 696 ms: 1.01x faster                                                |
| regex_v8                | 22.0 ms                                                             | 21.8 ms: 1.01x faster                                               |
| crypto_pyaes            | 73.8 ms                                                             | 73.3 ms: 1.01x faster                                               |
| genshi_text             | 21.8 ms                                                             | 21.7 ms: 1.01x faster                                               |
| chameleon               | 6.52 ms                                                             | 6.48 ms: 1.01x faster                                               |
| go                      | 138 ms                                                              | 139 ms: 1.01x slower                                                |
| async_tree_io           | 1.28 sec                                                            | 1.29 sec: 1.01x slower                                              |
| pyflate                 | 414 ms                                                              | 420 ms: 1.02x slower                                                |
| mdp                     | 2.64 sec                                                            | 2.68 sec: 1.02x slower                                              |
| thrift                  | 766 us                                                              | 780 us: 1.02x slower                                                |
| mako                    | 9.82 ms                                                             | 10.0 ms: 1.02x slower                                               |
| pickle_dict             | 30.9 us                                                             | 31.5 us: 1.02x slower                                               |
| xml_etree_process       | 54.1 ms                                                             | 55.3 ms: 1.02x slower                                               |
| regex_dna               | 196 ms                                                              | 204 ms: 1.04x slower                                                |
| python_startup          | 8.49 ms                                                             | 8.83 ms: 1.04x slower                                               |
| unpickle_list           | 4.96 us                                                             | 5.17 us: 1.04x slower                                               |
| pickle_list             | 4.03 us                                                             | 4.21 us: 1.04x slower                                               |
| sqlite_synth            | 2.51 us                                                             | 2.63 us: 1.04x slower                                               |
| xml_etree_generate      | 76.5 ms                                                             | 80.2 ms: 1.05x slower                                               |
| async_tree_memoization  | 621 ms                                                              | 652 ms: 1.05x slower                                                |
| unpickle                | 13.2 us                                                             | 13.9 us: 1.05x slower                                               |
| sqlglot_transpile       | 1.65 ms                                                             | 1.74 ms: 1.05x slower                                               |
| pickle                  | 9.79 us                                                             | 10.3 us: 1.05x slower                                               |
| sqlglot_parse           | 1.36 ms                                                             | 1.44 ms: 1.06x slower                                               |
| comprehensions          | 22.2 us                                                             | 23.6 us: 1.06x slower                                               |
| python_startup_no_site  | 5.98 ms                                                             | 6.53 ms: 1.09x slower                                               |
| regex_effbot            | 3.32 ms                                                             | 3.64 ms: 1.09x slower                                               |
| async_generators        | 361 ms                                                              | 410 ms: 1.14x slower                                                |
| dask                    | 368 ms                                                              | 511 ms: 1.39x slower                                                |
| Geometric mean          | (ref)                                                               | 1.03x faster                                                        |

Benchmark hidden because not significant (9): djangocms, scimark_lu, scimark_monte_carlo, async_tree_none, create_gc_cycles, django_template, bench_mp_pool, dulwich_log, async_tree_cpu_io_mixed
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
