
# Results vs. 3.11.0

- fork: thatbirdguythatuknownot
- ref: patch_30
- machine: linux-x86_64
- commit hash: 148c833
- commit date: 2023-04-15
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 249 ms: 1.03x faster                                                        |
| chameleon      | 6.52 ms                                                             | 6.48 ms: 1.01x faster                                                       |
| docutils       | 2.59 sec                                                            | 2.52 sec: 1.03x faster                                                      |
| html5lib       | 64.0 ms                                                             | 60.3 ms: 1.06x faster                                                       |
| tornado_http   | 96.7 ms                                                             | 93.0 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                               | 1.03x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 83.5 ms: 1.16x faster                                                       |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                        |
| float          | 76.0 ms                                                             | 73.7 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                               | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 129 ms: 1.06x faster                                                        |
| regex_v8       | 22.0 ms                                                             | 21.8 ms: 1.01x faster                                                       |
| regex_dna      | 196 ms                                                              | 207 ms: 1.05x slower                                                        |
| regex_effbot   | 3.32 ms                                                             | 3.52 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.32 ms: 1.35x faster                                                       |
| unpickle_pure_python | 228 us                                                              | 202 us: 1.13x faster                                                        |
| xml_etree_parse      | 162 ms                                                              | 150 ms: 1.08x faster                                                        |
| xml_etree_iterparse  | 108 ms                                                              | 99.8 ms: 1.08x faster                                                       |
| json_loads           | 26.2 us                                                             | 24.4 us: 1.07x faster                                                       |
| pickle_pure_python   | 307 us                                                              | 286 us: 1.07x faster                                                        |
| xml_etree_process    | 54.1 ms                                                             | 55.0 ms: 1.02x slower                                                       |
| pickle_dict          | 30.9 us                                                             | 31.7 us: 1.03x slower                                                       |
| unpickle_list        | 4.96 us                                                             | 5.15 us: 1.04x slower                                                       |
| xml_etree_generate   | 76.5 ms                                                             | 79.8 ms: 1.04x slower                                                       |
| pickle_list          | 4.03 us                                                             | 4.24 us: 1.05x slower                                                       |
| unpickle             | 13.2 us                                                             | 14.3 us: 1.08x slower                                                       |
| pickle               | 9.79 us                                                             | 10.7 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.90 ms: 1.05x slower                                                       |
| python_startup_no_site | 5.98 ms                                                             | 6.60 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                               | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 47.1 ms: 1.10x faster                                                       |
| genshi_text     | 21.8 ms                                                             | 21.5 ms: 1.01x faster                                                       |
| django_template | 32.9 ms                                                             | 32.7 ms: 1.01x faster                                                       |
| mako            | 9.82 ms                                                             | 9.96 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                               | 1.03x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 28.9 ms: 2.54x faster                                                       |
| asyncio_tcp             | 888 ms                                                              | 500 ms: 1.77x faster                                                        |
| json_dumps              | 12.5 ms                                                             | 9.32 ms: 1.35x faster                                                       |
| mypy2                   | 422 ms                                                              | 330 ms: 1.28x faster                                                        |
| coroutines              | 26.3 ms                                                             | 21.7 ms: 1.21x faster                                                       |
| nbody                   | 96.7 ms                                                             | 83.5 ms: 1.16x faster                                                       |
| unpack_sequence         | 49.5 ns                                                             | 42.9 ns: 1.15x faster                                                       |
| deltablue               | 3.66 ms                                                             | 3.23 ms: 1.13x faster                                                       |
| unpickle_pure_python    | 228 us                                                              | 202 us: 1.13x faster                                                        |
| sqlglot_parse           | 1.36 ms                                                             | 1.22 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.03 ms: 1.11x faster                                                       |
| sqlglot_transpile       | 1.65 ms                                                             | 1.50 ms: 1.10x faster                                                       |
| genshi_xml              | 51.8 ms                                                             | 47.1 ms: 1.10x faster                                                       |
| hexiom                  | 6.48 ms                                                             | 5.96 ms: 1.09x faster                                                       |
| spectral_norm           | 99.5 ms                                                             | 91.4 ms: 1.09x faster                                                       |
| pylint                  | 476 ms                                                              | 439 ms: 1.09x faster                                                        |
| xml_etree_parse         | 162 ms                                                              | 150 ms: 1.08x faster                                                        |
| xml_etree_iterparse     | 108 ms                                                              | 99.8 ms: 1.08x faster                                                       |
| richards                | 45.7 ms                                                             | 42.3 ms: 1.08x faster                                                       |
| json_loads              | 26.2 us                                                             | 24.4 us: 1.07x faster                                                       |
| pickle_pure_python      | 307 us                                                              | 286 us: 1.07x faster                                                        |
| html5lib                | 64.0 ms                                                             | 60.3 ms: 1.06x faster                                                       |
| pathlib                 | 18.2 ms                                                             | 17.2 ms: 1.06x faster                                                       |
| logging_simple          | 6.09 us                                                             | 5.76 us: 1.06x faster                                                       |
| scimark_fft             | 328 ms                                                              | 310 ms: 1.06x faster                                                        |
| regex_compile           | 137 ms                                                              | 129 ms: 1.06x faster                                                        |
| chaos                   | 68.0 ms                                                             | 64.8 ms: 1.05x faster                                                       |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                        |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.05x faster                                                       |
| scimark_sor             | 115 ms                                                              | 110 ms: 1.05x faster                                                        |
| sqlglot_normalize       | 108 ms                                                              | 104 ms: 1.05x faster                                                        |
| pycparser               | 1.14 sec                                                            | 1.10 sec: 1.04x faster                                                      |
| coverage                | 101 ms                                                              | 96.8 ms: 1.04x faster                                                       |
| logging_format          | 6.64 us                                                             | 6.36 us: 1.04x faster                                                       |
| gunicorn                | 1.13 ms                                                             | 1.08 ms: 1.04x faster                                                       |
| bench_thread_pool       | 820 us                                                              | 786 us: 1.04x faster                                                        |
| deepcopy_memo           | 36.4 us                                                             | 34.9 us: 1.04x faster                                                       |
| sqlglot_optimize        | 53.4 ms                                                             | 51.2 ms: 1.04x faster                                                       |
| comprehensions          | 22.2 us                                                             | 21.4 us: 1.04x faster                                                       |
| json                    | 4.86 ms                                                             | 4.67 ms: 1.04x faster                                                       |
| sympy_expand            | 477 ms                                                              | 459 ms: 1.04x faster                                                        |
| tornado_http            | 96.7 ms                                                             | 93.0 ms: 1.04x faster                                                       |
| sqlalchemy_imperative   | 18.0 ms                                                             | 17.3 ms: 1.04x faster                                                       |
| raytrace                | 292 ms                                                              | 282 ms: 1.04x faster                                                        |
| sympy_str               | 291 ms                                                              | 281 ms: 1.04x faster                                                        |
| mdp                     | 2.64 sec                                                            | 2.55 sec: 1.04x faster                                                      |
| nqueens                 | 84.0 ms                                                             | 81.1 ms: 1.04x faster                                                       |
| sympy_integrate         | 21.0 ms                                                             | 20.4 ms: 1.03x faster                                                       |
| 2to3                    | 257 ms                                                              | 249 ms: 1.03x faster                                                        |
| float                   | 76.0 ms                                                             | 73.7 ms: 1.03x faster                                                       |
| logging_silent          | 98.7 ns                                                             | 95.8 ns: 1.03x faster                                                       |
| scimark_lu              | 108 ms                                                              | 105 ms: 1.03x faster                                                        |
| docutils                | 2.59 sec                                                            | 2.52 sec: 1.03x faster                                                      |
| sympy_sum               | 167 ms                                                              | 163 ms: 1.03x faster                                                        |
| scimark_monte_carlo     | 67.8 ms                                                             | 66.2 ms: 1.02x faster                                                       |
| meteor_contest          | 106 ms                                                              | 104 ms: 1.02x faster                                                        |
| sqlalchemy_declarative  | 138 ms                                                              | 135 ms: 1.02x faster                                                        |
| dulwich_log             | 63.6 ms                                                             | 62.3 ms: 1.02x faster                                                       |
| go                      | 138 ms                                                              | 136 ms: 1.02x faster                                                        |
| telco                   | 6.59 ms                                                             | 6.48 ms: 1.02x faster                                                       |
| async_tree_none         | 525 ms                                                              | 517 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                              | 724 ms: 1.02x faster                                                        |
| deepcopy                | 339 us                                                              | 334 us: 1.01x faster                                                        |
| genshi_text             | 21.8 ms                                                             | 21.5 ms: 1.01x faster                                                       |
| create_gc_cycles        | 1.48 ms                                                             | 1.47 ms: 1.01x faster                                                       |
| pprint_pformat          | 1.45 sec                                                            | 1.44 sec: 1.01x faster                                                      |
| regex_v8                | 22.0 ms                                                             | 21.8 ms: 1.01x faster                                                       |
| django_template         | 32.9 ms                                                             | 32.7 ms: 1.01x faster                                                       |
| chameleon               | 6.52 ms                                                             | 6.48 ms: 1.01x faster                                                       |
| pprint_safe_repr        | 701 ms                                                              | 704 ms: 1.00x slower                                                        |
| fannkuch                | 384 ms                                                              | 387 ms: 1.01x slower                                                        |
| crypto_pyaes            | 73.8 ms                                                             | 74.5 ms: 1.01x slower                                                       |
| mako                    | 9.82 ms                                                             | 9.96 ms: 1.01x slower                                                       |
| xml_etree_process       | 54.1 ms                                                             | 55.0 ms: 1.02x slower                                                       |
| deepcopy_reduce         | 2.96 us                                                             | 3.02 us: 1.02x slower                                                       |
| pickle_dict             | 30.9 us                                                             | 31.7 us: 1.03x slower                                                       |
| thrift                  | 766 us                                                              | 792 us: 1.03x slower                                                        |
| unpickle_list           | 4.96 us                                                             | 5.15 us: 1.04x slower                                                       |
| xml_etree_generate      | 76.5 ms                                                             | 79.8 ms: 1.04x slower                                                       |
| python_startup          | 8.49 ms                                                             | 8.90 ms: 1.05x slower                                                       |
| sqlite_synth            | 2.51 us                                                             | 2.64 us: 1.05x slower                                                       |
| pickle_list             | 4.03 us                                                             | 4.24 us: 1.05x slower                                                       |
| regex_dna               | 196 ms                                                              | 207 ms: 1.05x slower                                                        |
| regex_effbot            | 3.32 ms                                                             | 3.52 ms: 1.06x slower                                                       |
| unpickle                | 13.2 us                                                             | 14.3 us: 1.08x slower                                                       |
| pickle                  | 9.79 us                                                             | 10.7 us: 1.09x slower                                                       |
| python_startup_no_site  | 5.98 ms                                                             | 6.60 ms: 1.10x slower                                                       |
| gc_traversal            | 3.63 ms                                                             | 4.06 ms: 1.12x slower                                                       |
| async_generators        | 361 ms                                                              | 427 ms: 1.18x slower                                                        |
| dask                    | 368 ms                                                              | 491 ms: 1.33x slower                                                        |
| Geometric mean          | (ref)                                                               | 1.04x faster                                                                |

Benchmark hidden because not significant (5): async_tree_memoization, djangocms, bench_mp_pool, async_tree_io, pyflate
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging
