
# Results vs. 3.11.0

- fork: python
- ref: dc3f97549a8fe4f7fea8
- machine: linux-x86_64
- commit hash: dc3f975
- commit date: 2023-04-26
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 268 ms: 1.04x slower                                                   |
| chameleon      | 6.52 ms                                                             | 6.94 ms: 1.07x slower                                                  |
| docutils       | 2.59 sec                                                            | 2.70 sec: 1.04x slower                                                 |
| html5lib       | 64.0 ms                                                             | 65.2 ms: 1.02x slower                                                  |
| tornado_http   | 96.7 ms                                                             | 105 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                               | 1.05x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 88.2 ms: 1.10x faster                                                  |
| pidigits       | 197 ms                                                              | 198 ms: 1.00x slower                                                   |
| float          | 76.0 ms                                                             | 80.0 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                               | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 22.2 ms: 1.01x slower                                                  |
| regex_dna      | 196 ms                                                              | 204 ms: 1.04x slower                                                   |
| regex_compile  | 137 ms                                                              | 145 ms: 1.06x slower                                                   |
| regex_effbot   | 3.32 ms                                                             | 3.75 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                               | 1.06x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 10.0 ms: 1.25x faster                                                  |
| xml_etree_parse      | 162 ms                                                              | 152 ms: 1.07x faster                                                   |
| unpickle_pure_python | 228 us                                                              | 218 us: 1.05x faster                                                   |
| xml_etree_iterparse  | 108 ms                                                              | 103 ms: 1.05x faster                                                   |
| json_loads           | 26.2 us                                                             | 25.8 us: 1.02x faster                                                  |
| unpickle_list        | 4.96 us                                                             | 4.90 us: 1.01x faster                                                  |
| pickle_pure_python   | 307 us                                                              | 313 us: 1.02x slower                                                   |
| pickle_dict          | 30.9 us                                                             | 31.6 us: 1.02x slower                                                  |
| xml_etree_process    | 54.1 ms                                                             | 58.6 ms: 1.08x slower                                                  |
| pickle               | 9.79 us                                                             | 10.7 us: 1.10x slower                                                  |
| xml_etree_generate   | 76.5 ms                                                             | 83.9 ms: 1.10x slower                                                  |
| unpickle             | 13.2 us                                                             | 15.0 us: 1.13x slower                                                  |
| pickle_list          | 4.03 us                                                             | 4.62 us: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.03 ms: 1.06x slower                                                  |
| python_startup_no_site | 5.98 ms                                                             | 6.62 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 21.8 ms                                                             | 22.7 ms: 1.04x slower                                                  |
| django_template | 32.9 ms                                                             | 34.7 ms: 1.05x slower                                                  |
| mako            | 9.82 ms                                                             | 10.9 ms: 1.11x slower                                                  |
| Geometric mean  | (ref)                                                               | 1.05x slower                                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 32.4 ms: 2.26x faster                                                  |
| asyncio_tcp             | 888 ms                                                              | 507 ms: 1.75x faster                                                   |
| json_dumps              | 12.5 ms                                                             | 10.0 ms: 1.25x faster                                                  |
| mypy2                   | 422 ms                                                              | 351 ms: 1.20x faster                                                   |
| coroutines              | 26.3 ms                                                             | 22.5 ms: 1.17x faster                                                  |
| nbody                   | 96.7 ms                                                             | 88.2 ms: 1.10x faster                                                  |
| xml_etree_parse         | 162 ms                                                              | 152 ms: 1.07x faster                                                   |
| unpack_sequence         | 49.5 ns                                                             | 46.6 ns: 1.06x faster                                                  |
| richards                | 45.7 ms                                                             | 43.4 ms: 1.05x faster                                                  |
| unpickle_pure_python    | 228 us                                                              | 218 us: 1.05x faster                                                   |
| xml_etree_iterparse     | 108 ms                                                              | 103 ms: 1.05x faster                                                   |
| deltablue               | 3.66 ms                                                             | 3.53 ms: 1.04x faster                                                  |
| hexiom                  | 6.48 ms                                                             | 6.27 ms: 1.03x faster                                                  |
| mdp                     | 2.64 sec                                                            | 2.57 sec: 1.03x faster                                                 |
| sqlglot_parse           | 1.36 ms                                                             | 1.33 ms: 1.02x faster                                                  |
| go                      | 138 ms                                                              | 135 ms: 1.02x faster                                                   |
| coverage                | 101 ms                                                              | 99.0 ms: 1.02x faster                                                  |
| json_loads              | 26.2 us                                                             | 25.8 us: 1.02x faster                                                  |
| unpickle_list           | 4.96 us                                                             | 4.90 us: 1.01x faster                                                  |
| create_gc_cycles        | 1.48 ms                                                             | 1.46 ms: 1.01x faster                                                  |
| pidigits                | 197 ms                                                              | 198 ms: 1.00x slower                                                   |
| nqueens                 | 84.0 ms                                                             | 84.5 ms: 1.01x slower                                                  |
| regex_v8                | 22.0 ms                                                             | 22.2 ms: 1.01x slower                                                  |
| logging_silent          | 98.7 ns                                                             | 99.9 ns: 1.01x slower                                                  |
| pathlib                 | 18.2 ms                                                             | 18.5 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 736 ms                                                              | 747 ms: 1.02x slower                                                   |
| sqlglot_optimize        | 53.4 ms                                                             | 54.3 ms: 1.02x slower                                                  |
| html5lib                | 64.0 ms                                                             | 65.2 ms: 1.02x slower                                                  |
| chaos                   | 68.0 ms                                                             | 69.3 ms: 1.02x slower                                                  |
| pickle_pure_python      | 307 us                                                              | 313 us: 1.02x slower                                                   |
| bench_thread_pool       | 820 us                                                              | 836 us: 1.02x slower                                                   |
| pickle_dict             | 30.9 us                                                             | 31.6 us: 1.02x slower                                                  |
| json                    | 4.86 ms                                                             | 4.96 ms: 1.02x slower                                                  |
| pprint_pformat          | 1.45 sec                                                            | 1.48 sec: 1.02x slower                                                 |
| logging_simple          | 6.09 us                                                             | 6.24 us: 1.02x slower                                                  |
| sqlglot_normalize       | 108 ms                                                              | 111 ms: 1.03x slower                                                   |
| telco                   | 6.59 ms                                                             | 6.78 ms: 1.03x slower                                                  |
| raytrace                | 292 ms                                                              | 302 ms: 1.03x slower                                                   |
| pprint_safe_repr        | 701 ms                                                              | 726 ms: 1.04x slower                                                   |
| scimark_lu              | 108 ms                                                              | 112 ms: 1.04x slower                                                   |
| regex_dna               | 196 ms                                                              | 204 ms: 1.04x slower                                                   |
| gc_traversal            | 3.63 ms                                                             | 3.76 ms: 1.04x slower                                                  |
| genshi_text             | 21.8 ms                                                             | 22.7 ms: 1.04x slower                                                  |
| sympy_integrate         | 21.0 ms                                                             | 21.9 ms: 1.04x slower                                                  |
| logging_format          | 6.64 us                                                             | 6.90 us: 1.04x slower                                                  |
| djangocms               | 32.3 us                                                             | 33.6 us: 1.04x slower                                                  |
| 2to3                    | 257 ms                                                              | 268 ms: 1.04x slower                                                   |
| docutils                | 2.59 sec                                                            | 2.70 sec: 1.04x slower                                                 |
| sympy_expand            | 477 ms                                                              | 501 ms: 1.05x slower                                                   |
| thrift                  | 766 us                                                              | 805 us: 1.05x slower                                                   |
| async_tree_memoization  | 621 ms                                                              | 654 ms: 1.05x slower                                                   |
| float                   | 76.0 ms                                                             | 80.0 ms: 1.05x slower                                                  |
| django_template         | 32.9 ms                                                             | 34.7 ms: 1.05x slower                                                  |
| sqlalchemy_declarative  | 138 ms                                                              | 146 ms: 1.05x slower                                                   |
| comprehensions          | 22.2 us                                                             | 23.5 us: 1.06x slower                                                  |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.1 ms: 1.06x slower                                                  |
| regex_compile           | 137 ms                                                              | 145 ms: 1.06x slower                                                   |
| python_startup          | 8.49 ms                                                             | 9.03 ms: 1.06x slower                                                  |
| chameleon               | 6.52 ms                                                             | 6.94 ms: 1.07x slower                                                  |
| dulwich_log             | 63.6 ms                                                             | 67.9 ms: 1.07x slower                                                  |
| deepcopy_memo           | 36.4 us                                                             | 39.0 us: 1.07x slower                                                  |
| sympy_str               | 291 ms                                                              | 312 ms: 1.07x slower                                                   |
| sqlite_synth            | 2.51 us                                                             | 2.70 us: 1.07x slower                                                  |
| scimark_monte_carlo     | 67.8 ms                                                             | 73.1 ms: 1.08x slower                                                  |
| crypto_pyaes            | 73.8 ms                                                             | 79.5 ms: 1.08x slower                                                  |
| xml_etree_process       | 54.1 ms                                                             | 58.6 ms: 1.08x slower                                                  |
| tornado_http            | 96.7 ms                                                             | 105 ms: 1.08x slower                                                   |
| sympy_sum               | 167 ms                                                              | 182 ms: 1.08x slower                                                   |
| deepcopy                | 339 us                                                              | 368 us: 1.09x slower                                                   |
| deepcopy_reduce         | 2.96 us                                                             | 3.22 us: 1.09x slower                                                  |
| meteor_contest          | 106 ms                                                              | 116 ms: 1.09x slower                                                   |
| pyflate                 | 414 ms                                                              | 451 ms: 1.09x slower                                                   |
| spectral_norm           | 99.5 ms                                                             | 108 ms: 1.09x slower                                                   |
| scimark_sor             | 115 ms                                                              | 126 ms: 1.10x slower                                                   |
| pickle                  | 9.79 us                                                             | 10.7 us: 1.10x slower                                                  |
| xml_etree_generate      | 76.5 ms                                                             | 83.9 ms: 1.10x slower                                                  |
| mako                    | 9.82 ms                                                             | 10.9 ms: 1.11x slower                                                  |
| python_startup_no_site  | 5.98 ms                                                             | 6.62 ms: 1.11x slower                                                  |
| scimark_fft             | 328 ms                                                              | 364 ms: 1.11x slower                                                   |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 5.00 ms: 1.12x slower                                                  |
| regex_effbot            | 3.32 ms                                                             | 3.75 ms: 1.13x slower                                                  |
| unpickle                | 13.2 us                                                             | 15.0 us: 1.13x slower                                                  |
| pickle_list             | 4.03 us                                                             | 4.62 us: 1.15x slower                                                  |
| async_generators        | 361 ms                                                              | 449 ms: 1.24x slower                                                   |
| dask                    | 368 ms                                                              | 541 ms: 1.47x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.02x slower                                                           |

Benchmark hidden because not significant (8): pylint, pycparser, genshi_xml, bench_mp_pool, sqlglot_transpile, async_tree_io, async_tree_none, fannkuch
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn
