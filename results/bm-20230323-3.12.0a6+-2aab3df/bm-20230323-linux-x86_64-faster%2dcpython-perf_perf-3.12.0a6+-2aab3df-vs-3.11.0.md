
# Results vs. 3.11.0

- fork: faster-cpython
- ref: perf_perf
- machine: linux-x86_64
- commit hash: 2aab3df
- commit date: 2023-03-23
- overall geometric mean: 1.05x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 271 ms: 1.05x slower                                                  |
| chameleon      | 6.52 ms                                                             | 7.07 ms: 1.08x slower                                                 |
| docutils       | 2.59 sec                                                            | 2.72 sec: 1.05x slower                                                |
| html5lib       | 64.0 ms                                                             | 68.3 ms: 1.07x slower                                                 |
| tornado_http   | 96.7 ms                                                             | 104 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                               | 1.07x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 89.0 ms: 1.09x faster                                                 |
| pidigits       | 197 ms                                                              | 189 ms: 1.04x faster                                                  |
| float          | 76.0 ms                                                             | 79.0 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                               | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                             | 3.40 ms: 1.02x slower                                                 |
| regex_v8       | 22.0 ms                                                             | 22.7 ms: 1.03x slower                                                 |
| regex_dna      | 196 ms                                                              | 206 ms: 1.05x slower                                                  |
| regex_compile  | 137 ms                                                              | 145 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                               | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.78 ms: 1.28x faster                                                 |
| xml_etree_parse      | 162 ms                                                              | 150 ms: 1.08x faster                                                  |
| json_loads           | 26.2 us                                                             | 24.4 us: 1.07x faster                                                 |
| xml_etree_iterparse  | 108 ms                                                              | 102 ms: 1.06x faster                                                  |
| pickle_dict          | 30.9 us                                                             | 30.5 us: 1.01x faster                                                 |
| pickle_list          | 4.03 us                                                             | 4.10 us: 1.02x slower                                                 |
| unpickle             | 13.2 us                                                             | 13.6 us: 1.03x slower                                                 |
| unpickle_pure_python | 228 us                                                              | 238 us: 1.04x slower                                                  |
| pickle               | 9.79 us                                                             | 10.3 us: 1.05x slower                                                 |
| unpickle_list        | 4.96 us                                                             | 5.20 us: 1.05x slower                                                 |
| pickle_pure_python   | 307 us                                                              | 337 us: 1.10x slower                                                  |
| xml_etree_generate   | 76.5 ms                                                             | 84.1 ms: 1.10x slower                                                 |
| xml_etree_process    | 54.1 ms                                                             | 60.6 ms: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                               | 1.00x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.52 ms: 1.12x slower                                                 |
| python_startup_no_site | 5.98 ms                                                             | 6.88 ms: 1.15x slower                                                 |
| Geometric mean         | (ref)                                                               | 1.14x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 52.2 ms: 1.01x slower                                                 |
| mako            | 9.82 ms                                                             | 10.6 ms: 1.08x slower                                                 |
| genshi_text     | 21.8 ms                                                             | 24.5 ms: 1.12x slower                                                 |
| django_template | 32.9 ms                                                             | 39.1 ms: 1.19x slower                                                 |
| Geometric mean  | (ref)                                                               | 1.10x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 29.4 ms: 2.50x faster                                                 |
| asyncio_tcp             | 888 ms                                                              | 522 ms: 1.70x faster                                                  |
| json_dumps              | 12.5 ms                                                             | 9.78 ms: 1.28x faster                                                 |
| unpack_sequence         | 49.5 ns                                                             | 42.7 ns: 1.16x faster                                                 |
| mypy2                   | 422 ms                                                              | 378 ms: 1.12x faster                                                  |
| nbody                   | 96.7 ms                                                             | 89.0 ms: 1.09x faster                                                 |
| scimark_fft             | 328 ms                                                              | 302 ms: 1.09x faster                                                  |
| xml_etree_parse         | 162 ms                                                              | 150 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.14 ms: 1.08x faster                                                 |
| json_loads              | 26.2 us                                                             | 24.4 us: 1.07x faster                                                 |
| xml_etree_iterparse     | 108 ms                                                              | 102 ms: 1.06x faster                                                  |
| pidigits                | 197 ms                                                              | 189 ms: 1.04x faster                                                  |
| json                    | 4.86 ms                                                             | 4.67 ms: 1.04x faster                                                 |
| meteor_contest          | 106 ms                                                              | 105 ms: 1.01x faster                                                  |
| pickle_dict             | 30.9 us                                                             | 30.5 us: 1.01x faster                                                 |
| create_gc_cycles        | 1.48 ms                                                             | 1.48 ms: 1.00x slower                                                 |
| mdp                     | 2.64 sec                                                            | 2.65 sec: 1.01x slower                                                |
| nqueens                 | 84.0 ms                                                             | 84.6 ms: 1.01x slower                                                 |
| fannkuch                | 384 ms                                                              | 387 ms: 1.01x slower                                                  |
| genshi_xml              | 51.8 ms                                                             | 52.2 ms: 1.01x slower                                                 |
| crypto_pyaes            | 73.8 ms                                                             | 74.8 ms: 1.01x slower                                                 |
| pickle_list             | 4.03 us                                                             | 4.10 us: 1.02x slower                                                 |
| coverage                | 101 ms                                                              | 103 ms: 1.02x slower                                                  |
| bench_thread_pool       | 820 us                                                              | 837 us: 1.02x slower                                                  |
| gunicorn                | 1.13 ms                                                             | 1.16 ms: 1.02x slower                                                 |
| regex_effbot            | 3.32 ms                                                             | 3.40 ms: 1.02x slower                                                 |
| unpickle                | 13.2 us                                                             | 13.6 us: 1.03x slower                                                 |
| pycparser               | 1.14 sec                                                            | 1.18 sec: 1.03x slower                                                |
| regex_v8                | 22.0 ms                                                             | 22.7 ms: 1.03x slower                                                 |
| chaos                   | 68.0 ms                                                             | 70.3 ms: 1.03x slower                                                 |
| aiohttp                 | 1.05 ms                                                             | 1.09 ms: 1.03x slower                                                 |
| djangocms               | 32.3 us                                                             | 33.4 us: 1.03x slower                                                 |
| float                   | 76.0 ms                                                             | 79.0 ms: 1.04x slower                                                 |
| sqlite_synth            | 2.51 us                                                             | 2.62 us: 1.04x slower                                                 |
| pathlib                 | 18.2 ms                                                             | 19.0 ms: 1.04x slower                                                 |
| unpickle_pure_python    | 228 us                                                              | 238 us: 1.04x slower                                                  |
| pickle                  | 9.79 us                                                             | 10.3 us: 1.05x slower                                                 |
| unpickle_list           | 4.96 us                                                             | 5.20 us: 1.05x slower                                                 |
| regex_dna               | 196 ms                                                              | 206 ms: 1.05x slower                                                  |
| docutils                | 2.59 sec                                                            | 2.72 sec: 1.05x slower                                                |
| sympy_expand            | 477 ms                                                              | 501 ms: 1.05x slower                                                  |
| 2to3                    | 257 ms                                                              | 271 ms: 1.05x slower                                                  |
| scimark_monte_carlo     | 67.8 ms                                                             | 71.9 ms: 1.06x slower                                                 |
| sympy_integrate         | 21.0 ms                                                             | 22.4 ms: 1.06x slower                                                 |
| regex_compile           | 137 ms                                                              | 145 ms: 1.07x slower                                                  |
| sympy_str               | 291 ms                                                              | 311 ms: 1.07x slower                                                  |
| html5lib                | 64.0 ms                                                             | 68.3 ms: 1.07x slower                                                 |
| coroutines              | 26.3 ms                                                             | 28.0 ms: 1.07x slower                                                 |
| sympy_sum               | 167 ms                                                              | 179 ms: 1.07x slower                                                  |
| sqlalchemy_declarative  | 138 ms                                                              | 148 ms: 1.07x slower                                                  |
| tornado_http            | 96.7 ms                                                             | 104 ms: 1.07x slower                                                  |
| async_tree_cpu_io_mixed | 736 ms                                                              | 793 ms: 1.08x slower                                                  |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.5 ms: 1.08x slower                                                 |
| async_tree_io           | 1.28 sec                                                            | 1.39 sec: 1.08x slower                                                |
| async_tree_none         | 525 ms                                                              | 568 ms: 1.08x slower                                                  |
| mako                    | 9.82 ms                                                             | 10.6 ms: 1.08x slower                                                 |
| thrift                  | 766 us                                                              | 830 us: 1.08x slower                                                  |
| chameleon               | 6.52 ms                                                             | 7.07 ms: 1.08x slower                                                 |
| spectral_norm           | 99.5 ms                                                             | 108 ms: 1.08x slower                                                  |
| hexiom                  | 6.48 ms                                                             | 7.09 ms: 1.09x slower                                                 |
| pprint_pformat          | 1.45 sec                                                            | 1.59 sec: 1.09x slower                                                |
| pickle_pure_python      | 307 us                                                              | 337 us: 1.10x slower                                                  |
| sqlglot_optimize        | 53.4 ms                                                             | 58.5 ms: 1.10x slower                                                 |
| pprint_safe_repr        | 701 ms                                                              | 770 ms: 1.10x slower                                                  |
| xml_etree_generate      | 76.5 ms                                                             | 84.1 ms: 1.10x slower                                                 |
| dulwich_log             | 63.6 ms                                                             | 69.9 ms: 1.10x slower                                                 |
| async_tree_memoization  | 621 ms                                                              | 684 ms: 1.10x slower                                                  |
| scimark_sor             | 115 ms                                                              | 127 ms: 1.11x slower                                                  |
| deepcopy                | 339 us                                                              | 377 us: 1.11x slower                                                  |
| sqlglot_normalize       | 108 ms                                                              | 121 ms: 1.11x slower                                                  |
| xml_etree_process       | 54.1 ms                                                             | 60.6 ms: 1.12x slower                                                 |
| genshi_text             | 21.8 ms                                                             | 24.5 ms: 1.12x slower                                                 |
| python_startup          | 8.49 ms                                                             | 9.52 ms: 1.12x slower                                                 |
| deepcopy_memo           | 36.4 us                                                             | 41.2 us: 1.13x slower                                                 |
| deepcopy_reduce         | 2.96 us                                                             | 3.35 us: 1.13x slower                                                 |
| python_startup_no_site  | 5.98 ms                                                             | 6.88 ms: 1.15x slower                                                 |
| raytrace                | 292 ms                                                              | 337 ms: 1.15x slower                                                  |
| pyflate                 | 414 ms                                                              | 478 ms: 1.16x slower                                                  |
| go                      | 138 ms                                                              | 161 ms: 1.17x slower                                                  |
| comprehensions          | 22.2 us                                                             | 26.0 us: 1.17x slower                                                 |
| django_template         | 32.9 ms                                                             | 39.1 ms: 1.19x slower                                                 |
| gc_traversal            | 3.63 ms                                                             | 4.32 ms: 1.19x slower                                                 |
| richards                | 45.7 ms                                                             | 54.6 ms: 1.19x slower                                                 |
| sqlglot_transpile       | 1.65 ms                                                             | 1.99 ms: 1.21x slower                                                 |
| async_generators        | 361 ms                                                              | 436 ms: 1.21x slower                                                  |
| sqlglot_parse           | 1.36 ms                                                             | 1.66 ms: 1.22x slower                                                 |
| deltablue               | 3.66 ms                                                             | 4.47 ms: 1.22x slower                                                 |
| logging_simple          | 6.09 us                                                             | 7.48 us: 1.23x slower                                                 |
| logging_format          | 6.64 us                                                             | 8.20 us: 1.24x slower                                                 |
| logging_silent          | 98.7 ns                                                             | 130 ns: 1.32x slower                                                  |
| dask                    | 368 ms                                                              | 557 ms: 1.51x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.05x slower                                                          |

Benchmark hidden because not significant (3): scimark_lu, telco, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
