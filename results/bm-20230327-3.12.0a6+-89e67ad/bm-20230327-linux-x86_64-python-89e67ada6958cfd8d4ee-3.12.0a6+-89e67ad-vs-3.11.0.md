
# Results vs. 3.11.0

- fork: python
- ref: 89e67ada6958cfd8d4ee
- machine: linux-x86_64
- commit hash: 89e67ad
- commit date: 2023-03-27
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 251 ms: 1.02x faster                                                   |
| chameleon      | 6.52 ms                                                             | 6.46 ms: 1.01x faster                                                  |
| docutils       | 2.59 sec                                                            | 2.53 sec: 1.02x faster                                                 |
| html5lib       | 64.0 ms                                                             | 62.0 ms: 1.03x faster                                                  |
| tornado_http   | 96.7 ms                                                             | 91.2 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                               | 1.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 87.3 ms: 1.11x faster                                                  |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                   |
| float          | 76.0 ms                                                             | 73.4 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                               | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 134 ms: 1.02x faster                                                   |
| regex_v8       | 22.0 ms                                                             | 21.8 ms: 1.01x faster                                                  |
| regex_effbot   | 3.32 ms                                                             | 3.43 ms: 1.03x slower                                                  |
| regex_dna      | 196 ms                                                              | 203 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                               | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.52 ms: 1.32x faster                                                  |
| unpickle_pure_python | 228 us                                                              | 200 us: 1.14x faster                                                   |
| xml_etree_parse      | 162 ms                                                              | 149 ms: 1.09x faster                                                   |
| json_loads           | 26.2 us                                                             | 24.1 us: 1.09x faster                                                  |
| xml_etree_iterparse  | 108 ms                                                              | 100 ms: 1.07x faster                                                   |
| pickle_pure_python   | 307 us                                                              | 288 us: 1.07x faster                                                   |
| pickle_dict          | 30.9 us                                                             | 31.2 us: 1.01x slower                                                  |
| unpickle_list        | 4.96 us                                                             | 5.08 us: 1.02x slower                                                  |
| pickle_list          | 4.03 us                                                             | 4.15 us: 1.03x slower                                                  |
| xml_etree_process    | 54.1 ms                                                             | 56.0 ms: 1.04x slower                                                  |
| pickle               | 9.79 us                                                             | 10.2 us: 1.04x slower                                                  |
| xml_etree_generate   | 76.5 ms                                                             | 80.9 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.04x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.80 ms: 1.04x slower                                                  |
| python_startup_no_site | 5.98 ms                                                             | 6.50 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 47.4 ms: 1.09x faster                                                  |
| django_template | 32.9 ms                                                             | 33.1 ms: 1.01x slower                                                  |
| mako            | 9.82 ms                                                             | 9.95 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                               | 1.02x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 28.9 ms: 2.55x faster                                                  |
| asyncio_tcp             | 888 ms                                                              | 502 ms: 1.77x faster                                                   |
| json_dumps              | 12.5 ms                                                             | 9.52 ms: 1.32x faster                                                  |
| mypy2                   | 422 ms                                                              | 332 ms: 1.27x faster                                                   |
| unpack_sequence         | 49.5 ns                                                             | 41.8 ns: 1.18x faster                                                  |
| coroutines              | 26.3 ms                                                             | 22.9 ms: 1.14x faster                                                  |
| unpickle_pure_python    | 228 us                                                              | 200 us: 1.14x faster                                                   |
| deltablue               | 3.66 ms                                                             | 3.20 ms: 1.14x faster                                                  |
| nbody                   | 96.7 ms                                                             | 87.3 ms: 1.11x faster                                                  |
| genshi_xml              | 51.8 ms                                                             | 47.4 ms: 1.09x faster                                                  |
| xml_etree_parse         | 162 ms                                                              | 149 ms: 1.09x faster                                                   |
| json_loads              | 26.2 us                                                             | 24.1 us: 1.09x faster                                                  |
| spectral_norm           | 99.5 ms                                                             | 91.8 ms: 1.08x faster                                                  |
| deepcopy_memo           | 36.4 us                                                             | 33.6 us: 1.08x faster                                                  |
| hexiom                  | 6.48 ms                                                             | 6.02 ms: 1.08x faster                                                  |
| xml_etree_iterparse     | 108 ms                                                              | 100 ms: 1.07x faster                                                   |
| pickle_pure_python      | 307 us                                                              | 288 us: 1.07x faster                                                   |
| tornado_http            | 96.7 ms                                                             | 91.2 ms: 1.06x faster                                                  |
| logging_simple          | 6.09 us                                                             | 5.77 us: 1.06x faster                                                  |
| mdp                     | 2.64 sec                                                            | 2.51 sec: 1.05x faster                                                 |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.25 ms: 1.05x faster                                                  |
| richards                | 45.7 ms                                                             | 43.5 ms: 1.05x faster                                                  |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                   |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.05x faster                                                  |
| json                    | 4.86 ms                                                             | 4.64 ms: 1.05x faster                                                  |
| scimark_fft             | 328 ms                                                              | 313 ms: 1.05x faster                                                   |
| coverage                | 101 ms                                                              | 96.7 ms: 1.05x faster                                                  |
| logging_silent          | 98.7 ns                                                             | 94.5 ns: 1.05x faster                                                  |
| nqueens                 | 84.0 ms                                                             | 80.4 ms: 1.04x faster                                                  |
| logging_format          | 6.64 us                                                             | 6.37 us: 1.04x faster                                                  |
| bench_thread_pool       | 820 us                                                              | 788 us: 1.04x faster                                                   |
| raytrace                | 292 ms                                                              | 282 ms: 1.04x faster                                                   |
| sympy_expand            | 477 ms                                                              | 460 ms: 1.04x faster                                                   |
| sqlglot_optimize        | 53.4 ms                                                             | 51.5 ms: 1.04x faster                                                  |
| float                   | 76.0 ms                                                             | 73.4 ms: 1.03x faster                                                  |
| gunicorn                | 1.13 ms                                                             | 1.09 ms: 1.03x faster                                                  |
| pathlib                 | 18.2 ms                                                             | 17.6 ms: 1.03x faster                                                  |
| scimark_sor             | 115 ms                                                              | 111 ms: 1.03x faster                                                   |
| deepcopy                | 339 us                                                              | 328 us: 1.03x faster                                                   |
| sqlalchemy_imperative   | 18.0 ms                                                             | 17.5 ms: 1.03x faster                                                  |
| html5lib                | 64.0 ms                                                             | 62.0 ms: 1.03x faster                                                  |
| sympy_str               | 291 ms                                                              | 283 ms: 1.03x faster                                                   |
| sympy_integrate         | 21.0 ms                                                             | 20.4 ms: 1.03x faster                                                  |
| pycparser               | 1.14 sec                                                            | 1.11 sec: 1.03x faster                                                 |
| docutils                | 2.59 sec                                                            | 2.53 sec: 1.02x faster                                                 |
| 2to3                    | 257 ms                                                              | 251 ms: 1.02x faster                                                   |
| telco                   | 6.59 ms                                                             | 6.46 ms: 1.02x faster                                                  |
| sqlalchemy_declarative  | 138 ms                                                              | 136 ms: 1.02x faster                                                   |
| sympy_sum               | 167 ms                                                              | 164 ms: 1.02x faster                                                   |
| chaos                   | 68.0 ms                                                             | 66.7 ms: 1.02x faster                                                  |
| pprint_pformat          | 1.45 sec                                                            | 1.43 sec: 1.02x faster                                                 |
| sqlglot_normalize       | 108 ms                                                              | 107 ms: 1.02x faster                                                   |
| regex_compile           | 137 ms                                                              | 134 ms: 1.02x faster                                                   |
| meteor_contest          | 106 ms                                                              | 105 ms: 1.02x faster                                                   |
| deepcopy_reduce         | 2.96 us                                                             | 2.92 us: 1.01x faster                                                  |
| chameleon               | 6.52 ms                                                             | 6.46 ms: 1.01x faster                                                  |
| create_gc_cycles        | 1.48 ms                                                             | 1.47 ms: 1.01x faster                                                  |
| dulwich_log             | 63.6 ms                                                             | 63.1 ms: 1.01x faster                                                  |
| pprint_safe_repr        | 701 ms                                                              | 696 ms: 1.01x faster                                                   |
| regex_v8                | 22.0 ms                                                             | 21.8 ms: 1.01x faster                                                  |
| django_template         | 32.9 ms                                                             | 33.1 ms: 1.01x slower                                                  |
| go                      | 138 ms                                                              | 139 ms: 1.01x slower                                                   |
| pickle_dict             | 30.9 us                                                             | 31.2 us: 1.01x slower                                                  |
| async_tree_io           | 1.28 sec                                                            | 1.29 sec: 1.01x slower                                                 |
| pyflate                 | 414 ms                                                              | 418 ms: 1.01x slower                                                   |
| gc_traversal            | 3.63 ms                                                             | 3.67 ms: 1.01x slower                                                  |
| mako                    | 9.82 ms                                                             | 9.95 ms: 1.01x slower                                                  |
| scimark_lu              | 108 ms                                                              | 110 ms: 1.02x slower                                                   |
| scimark_monte_carlo     | 67.8 ms                                                             | 69.1 ms: 1.02x slower                                                  |
| thrift                  | 766 us                                                              | 781 us: 1.02x slower                                                   |
| unpickle_list           | 4.96 us                                                             | 5.08 us: 1.02x slower                                                  |
| pickle_list             | 4.03 us                                                             | 4.15 us: 1.03x slower                                                  |
| regex_effbot            | 3.32 ms                                                             | 3.43 ms: 1.03x slower                                                  |
| sqlite_synth            | 2.51 us                                                             | 2.60 us: 1.03x slower                                                  |
| regex_dna               | 196 ms                                                              | 203 ms: 1.03x slower                                                   |
| xml_etree_process       | 54.1 ms                                                             | 56.0 ms: 1.04x slower                                                  |
| python_startup          | 8.49 ms                                                             | 8.80 ms: 1.04x slower                                                  |
| pickle                  | 9.79 us                                                             | 10.2 us: 1.04x slower                                                  |
| sqlglot_transpile       | 1.65 ms                                                             | 1.73 ms: 1.04x slower                                                  |
| sqlglot_parse           | 1.36 ms                                                             | 1.43 ms: 1.05x slower                                                  |
| async_tree_memoization  | 621 ms                                                              | 656 ms: 1.06x slower                                                   |
| xml_etree_generate      | 76.5 ms                                                             | 80.9 ms: 1.06x slower                                                  |
| comprehensions          | 22.2 us                                                             | 23.8 us: 1.07x slower                                                  |
| python_startup_no_site  | 5.98 ms                                                             | 6.50 ms: 1.09x slower                                                  |
| async_generators        | 361 ms                                                              | 410 ms: 1.14x slower                                                   |
| dask                    | 368 ms                                                              | 510 ms: 1.38x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.04x faster                                                           |

Benchmark hidden because not significant (8): genshi_text, crypto_pyaes, fannkuch, async_tree_none, bench_mp_pool, async_tree_cpu_io_mixed, unpickle, djangocms
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
