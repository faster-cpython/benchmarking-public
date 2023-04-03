
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_call
- machine: linux-x86_64
- commit hash: 29928ee
- commit date: 2023-03-25
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 251 ms: 1.02x faster                                                |
| chameleon      | 6.52 ms                                                             | 6.55 ms: 1.00x slower                                               |
| docutils       | 2.59 sec                                                            | 2.54 sec: 1.02x faster                                              |
| html5lib       | 64.0 ms                                                             | 61.5 ms: 1.04x faster                                               |
| tornado_http   | 96.7 ms                                                             | 91.4 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                               | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 87.9 ms: 1.10x faster                                               |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                |
| float          | 76.0 ms                                                             | 74.7 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                               | 1.05x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 21.4 ms: 1.03x faster                                               |
| regex_compile  | 137 ms                                                              | 135 ms: 1.01x faster                                                |
| regex_effbot   | 3.32 ms                                                             | 3.45 ms: 1.04x slower                                               |
| regex_dna      | 196 ms                                                              | 207 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                               | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.48 ms: 1.32x faster                                               |
| unpickle_pure_python | 228 us                                                              | 202 us: 1.13x faster                                                |
| xml_etree_parse      | 162 ms                                                              | 149 ms: 1.09x faster                                                |
| json_loads           | 26.2 us                                                             | 24.4 us: 1.07x faster                                               |
| pickle_pure_python   | 307 us                                                              | 288 us: 1.07x faster                                                |
| xml_etree_iterparse  | 108 ms                                                              | 102 ms: 1.06x faster                                                |
| pickle_dict          | 30.9 us                                                             | 30.7 us: 1.01x faster                                               |
| pickle_list          | 4.03 us                                                             | 4.12 us: 1.02x slower                                               |
| unpickle             | 13.2 us                                                             | 13.6 us: 1.03x slower                                               |
| xml_etree_process    | 54.1 ms                                                             | 55.9 ms: 1.03x slower                                               |
| pickle               | 9.79 us                                                             | 10.2 us: 1.04x slower                                               |
| unpickle_list        | 4.96 us                                                             | 5.23 us: 1.05x slower                                               |
| xml_etree_generate   | 76.5 ms                                                             | 81.4 ms: 1.06x slower                                               |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.85 ms: 1.04x slower                                               |
| python_startup_no_site | 5.98 ms                                                             | 6.55 ms: 1.10x slower                                               |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 46.9 ms: 1.11x faster                                               |
| genshi_text     | 21.8 ms                                                             | 21.2 ms: 1.03x faster                                               |
| django_template | 32.9 ms                                                             | 33.3 ms: 1.01x slower                                               |
| mako            | 9.82 ms                                                             | 9.98 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                               | 1.02x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|-------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 30.2 ms: 2.43x faster                                               |
| asyncio_tcp             | 888 ms                                                              | 504 ms: 1.76x faster                                                |
| json_dumps              | 12.5 ms                                                             | 9.48 ms: 1.32x faster                                               |
| mypy2                   | 422 ms                                                              | 333 ms: 1.27x faster                                                |
| deltablue               | 3.66 ms                                                             | 3.21 ms: 1.14x faster                                               |
| unpickle_pure_python    | 228 us                                                              | 202 us: 1.13x faster                                                |
| unpack_sequence         | 49.5 ns                                                             | 44.0 ns: 1.13x faster                                               |
| coroutines              | 26.3 ms                                                             | 23.5 ms: 1.12x faster                                               |
| genshi_xml              | 51.8 ms                                                             | 46.9 ms: 1.11x faster                                               |
| nbody                   | 96.7 ms                                                             | 87.9 ms: 1.10x faster                                               |
| xml_etree_parse         | 162 ms                                                              | 149 ms: 1.09x faster                                                |
| deepcopy_memo           | 36.4 us                                                             | 33.7 us: 1.08x faster                                               |
| hexiom                  | 6.48 ms                                                             | 6.03 ms: 1.07x faster                                               |
| json_loads              | 26.2 us                                                             | 24.4 us: 1.07x faster                                               |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.18 ms: 1.07x faster                                               |
| pickle_pure_python      | 307 us                                                              | 288 us: 1.07x faster                                                |
| logging_simple          | 6.09 us                                                             | 5.73 us: 1.06x faster                                               |
| xml_etree_iterparse     | 108 ms                                                              | 102 ms: 1.06x faster                                                |
| tornado_http            | 96.7 ms                                                             | 91.4 ms: 1.06x faster                                               |
| mdp                     | 2.64 sec                                                            | 2.50 sec: 1.06x faster                                              |
| scimark_fft             | 328 ms                                                              | 310 ms: 1.06x faster                                                |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                |
| json                    | 4.86 ms                                                             | 4.65 ms: 1.05x faster                                               |
| bench_thread_pool       | 820 us                                                              | 784 us: 1.04x faster                                                |
| pathlib                 | 18.2 ms                                                             | 17.4 ms: 1.04x faster                                               |
| logging_format          | 6.64 us                                                             | 6.36 us: 1.04x faster                                               |
| nqueens                 | 84.0 ms                                                             | 80.6 ms: 1.04x faster                                               |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.04x faster                                               |
| html5lib                | 64.0 ms                                                             | 61.5 ms: 1.04x faster                                               |
| gunicorn                | 1.13 ms                                                             | 1.09 ms: 1.04x faster                                               |
| deepcopy                | 339 us                                                              | 327 us: 1.04x faster                                                |
| sqlglot_optimize        | 53.4 ms                                                             | 51.5 ms: 1.04x faster                                               |
| richards                | 45.7 ms                                                             | 44.2 ms: 1.03x faster                                               |
| chaos                   | 68.0 ms                                                             | 65.8 ms: 1.03x faster                                               |
| sympy_expand            | 477 ms                                                              | 462 ms: 1.03x faster                                                |
| sympy_integrate         | 21.0 ms                                                             | 20.5 ms: 1.03x faster                                               |
| genshi_text             | 21.8 ms                                                             | 21.2 ms: 1.03x faster                                               |
| sqlglot_normalize       | 108 ms                                                              | 105 ms: 1.03x faster                                                |
| pprint_pformat          | 1.45 sec                                                            | 1.41 sec: 1.03x faster                                              |
| scimark_sor             | 115 ms                                                              | 112 ms: 1.03x faster                                                |
| raytrace                | 292 ms                                                              | 285 ms: 1.03x faster                                                |
| regex_v8                | 22.0 ms                                                             | 21.4 ms: 1.03x faster                                               |
| 2to3                    | 257 ms                                                              | 251 ms: 1.02x faster                                                |
| sympy_str               | 291 ms                                                              | 285 ms: 1.02x faster                                                |
| pprint_safe_repr        | 701 ms                                                              | 686 ms: 1.02x faster                                                |
| spectral_norm           | 99.5 ms                                                             | 97.3 ms: 1.02x faster                                               |
| coverage                | 101 ms                                                              | 99.1 ms: 1.02x faster                                               |
| meteor_contest          | 106 ms                                                              | 104 ms: 1.02x faster                                                |
| docutils                | 2.59 sec                                                            | 2.54 sec: 1.02x faster                                              |
| logging_silent          | 98.7 ns                                                             | 97.0 ns: 1.02x faster                                               |
| float                   | 76.0 ms                                                             | 74.7 ms: 1.02x faster                                               |
| scimark_monte_carlo     | 67.8 ms                                                             | 66.7 ms: 1.02x faster                                               |
| regex_compile           | 137 ms                                                              | 135 ms: 1.01x faster                                                |
| scimark_lu              | 108 ms                                                              | 107 ms: 1.01x faster                                                |
| crypto_pyaes            | 73.8 ms                                                             | 73.1 ms: 1.01x faster                                               |
| pickle_dict             | 30.9 us                                                             | 30.7 us: 1.01x faster                                               |
| go                      | 138 ms                                                              | 138 ms: 1.01x faster                                                |
| sympy_sum               | 167 ms                                                              | 167 ms: 1.00x faster                                                |
| chameleon               | 6.52 ms                                                             | 6.55 ms: 1.00x slower                                               |
| async_tree_io           | 1.28 sec                                                            | 1.29 sec: 1.01x slower                                              |
| sqlalchemy_declarative  | 138 ms                                                              | 140 ms: 1.01x slower                                                |
| django_template         | 32.9 ms                                                             | 33.3 ms: 1.01x slower                                               |
| create_gc_cycles        | 1.48 ms                                                             | 1.50 ms: 1.02x slower                                               |
| mako                    | 9.82 ms                                                             | 9.98 ms: 1.02x slower                                               |
| pickle_list             | 4.03 us                                                             | 4.12 us: 1.02x slower                                               |
| thrift                  | 766 us                                                              | 783 us: 1.02x slower                                                |
| unpickle                | 13.2 us                                                             | 13.6 us: 1.03x slower                                               |
| async_tree_memoization  | 621 ms                                                              | 638 ms: 1.03x slower                                                |
| xml_etree_process       | 54.1 ms                                                             | 55.9 ms: 1.03x slower                                               |
| regex_effbot            | 3.32 ms                                                             | 3.45 ms: 1.04x slower                                               |
| sqlite_synth            | 2.51 us                                                             | 2.61 us: 1.04x slower                                               |
| pyflate                 | 414 ms                                                              | 431 ms: 1.04x slower                                                |
| python_startup          | 8.49 ms                                                             | 8.85 ms: 1.04x slower                                               |
| pickle                  | 9.79 us                                                             | 10.2 us: 1.04x slower                                               |
| sqlglot_transpile       | 1.65 ms                                                             | 1.73 ms: 1.05x slower                                               |
| regex_dna               | 196 ms                                                              | 207 ms: 1.05x slower                                                |
| unpickle_list           | 4.96 us                                                             | 5.23 us: 1.05x slower                                               |
| sqlglot_parse           | 1.36 ms                                                             | 1.44 ms: 1.06x slower                                               |
| gc_traversal            | 3.63 ms                                                             | 3.83 ms: 1.06x slower                                               |
| xml_etree_generate      | 76.5 ms                                                             | 81.4 ms: 1.06x slower                                               |
| comprehensions          | 22.2 us                                                             | 23.7 us: 1.07x slower                                               |
| python_startup_no_site  | 5.98 ms                                                             | 6.55 ms: 1.10x slower                                               |
| async_generators        | 361 ms                                                              | 408 ms: 1.13x slower                                                |
| dask                    | 368 ms                                                              | 512 ms: 1.39x slower                                                |
| Geometric mean          | (ref)                                                               | 1.03x faster                                                        |

Benchmark hidden because not significant (10): sqlalchemy_imperative, async_tree_none, telco, dulwich_log, pycparser, bench_mp_pool, deepcopy_reduce, fannkuch, djangocms, async_tree_cpu_io_mixed
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
