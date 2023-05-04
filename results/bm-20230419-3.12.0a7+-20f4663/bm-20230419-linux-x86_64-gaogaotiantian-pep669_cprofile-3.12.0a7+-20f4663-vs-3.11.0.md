
# Results vs. 3.11.0

- fork: gaogaotiantian
- ref: pep669_cprofile
- machine: linux-x86_64
- commit hash: 20f4663
- commit date: 2023-04-19
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 250 ms: 1.03x faster                                                      |
| chameleon      | 6.52 ms                                                             | 6.26 ms: 1.04x faster                                                     |
| docutils       | 2.59 sec                                                            | 2.53 sec: 1.02x faster                                                    |
| html5lib       | 64.0 ms                                                             | 60.6 ms: 1.06x faster                                                     |
| tornado_http   | 96.7 ms                                                             | 92.7 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                               | 1.04x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 85.1 ms: 1.14x faster                                                     |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                      |
| float          | 76.0 ms                                                             | 73.1 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                               | 1.07x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 131 ms: 1.05x faster                                                      |
| regex_v8       | 22.0 ms                                                             | 21.3 ms: 1.03x faster                                                     |
| regex_dna      | 196 ms                                                              | 207 ms: 1.06x slower                                                      |
| regex_effbot   | 3.32 ms                                                             | 3.53 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                               | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.37 ms: 1.34x faster                                                     |
| unpickle_pure_python | 228 us                                                              | 201 us: 1.14x faster                                                      |
| xml_etree_parse      | 162 ms                                                              | 147 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 108 ms                                                              | 98.8 ms: 1.09x faster                                                     |
| pickle_pure_python   | 307 us                                                              | 283 us: 1.09x faster                                                      |
| json_loads           | 26.2 us                                                             | 24.1 us: 1.09x faster                                                     |
| xml_etree_process    | 54.1 ms                                                             | 55.8 ms: 1.03x slower                                                     |
| pickle_list          | 4.03 us                                                             | 4.24 us: 1.05x slower                                                     |
| unpickle             | 13.2 us                                                             | 13.9 us: 1.05x slower                                                     |
| pickle_dict          | 30.9 us                                                             | 32.6 us: 1.05x slower                                                     |
| xml_etree_generate   | 76.5 ms                                                             | 80.7 ms: 1.05x slower                                                     |
| pickle               | 9.79 us                                                             | 10.9 us: 1.11x slower                                                     |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.87 ms: 1.04x slower                                                     |
| python_startup_no_site | 5.98 ms                                                             | 6.57 ms: 1.10x slower                                                     |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 46.2 ms: 1.12x faster                                                     |
| genshi_text     | 21.8 ms                                                             | 21.3 ms: 1.03x faster                                                     |
| django_template | 32.9 ms                                                             | 32.6 ms: 1.01x faster                                                     |
| mako            | 9.82 ms                                                             | 9.94 ms: 1.01x slower                                                     |
| Geometric mean  | (ref)                                                               | 1.03x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|-------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 28.3 ms: 2.60x faster                                                     |
| asyncio_tcp             | 888 ms                                                              | 500 ms: 1.77x faster                                                      |
| json_dumps              | 12.5 ms                                                             | 9.37 ms: 1.34x faster                                                     |
| mypy2                   | 422 ms                                                              | 329 ms: 1.28x faster                                                      |
| coroutines              | 26.3 ms                                                             | 22.1 ms: 1.19x faster                                                     |
| unpack_sequence         | 49.5 ns                                                             | 42.8 ns: 1.16x faster                                                     |
| deltablue               | 3.66 ms                                                             | 3.19 ms: 1.15x faster                                                     |
| unpickle_pure_python    | 228 us                                                              | 201 us: 1.14x faster                                                      |
| nbody                   | 96.7 ms                                                             | 85.1 ms: 1.14x faster                                                     |
| sqlglot_parse           | 1.36 ms                                                             | 1.20 ms: 1.13x faster                                                     |
| genshi_xml              | 51.8 ms                                                             | 46.2 ms: 1.12x faster                                                     |
| sqlglot_transpile       | 1.65 ms                                                             | 1.49 ms: 1.11x faster                                                     |
| richards                | 45.7 ms                                                             | 41.3 ms: 1.11x faster                                                     |
| xml_etree_parse         | 162 ms                                                              | 147 ms: 1.10x faster                                                      |
| pylint                  | 476 ms                                                              | 435 ms: 1.10x faster                                                      |
| spectral_norm           | 99.5 ms                                                             | 90.9 ms: 1.09x faster                                                     |
| scimark_fft             | 328 ms                                                              | 300 ms: 1.09x faster                                                      |
| xml_etree_iterparse     | 108 ms                                                              | 98.8 ms: 1.09x faster                                                     |
| hexiom                  | 6.48 ms                                                             | 5.96 ms: 1.09x faster                                                     |
| pickle_pure_python      | 307 us                                                              | 283 us: 1.09x faster                                                      |
| json_loads              | 26.2 us                                                             | 24.1 us: 1.09x faster                                                     |
| pathlib                 | 18.2 ms                                                             | 17.0 ms: 1.07x faster                                                     |
| deepcopy_memo           | 36.4 us                                                             | 34.2 us: 1.06x faster                                                     |
| logging_simple          | 6.09 us                                                             | 5.74 us: 1.06x faster                                                     |
| sqlglot_normalize       | 108 ms                                                              | 102 ms: 1.06x faster                                                      |
| raytrace                | 292 ms                                                              | 276 ms: 1.06x faster                                                      |
| scimark_sor             | 115 ms                                                              | 109 ms: 1.06x faster                                                      |
| aiohttp                 | 1.05 ms                                                             | 998 us: 1.06x faster                                                      |
| nqueens                 | 84.0 ms                                                             | 79.5 ms: 1.06x faster                                                     |
| html5lib                | 64.0 ms                                                             | 60.6 ms: 1.06x faster                                                     |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.25 ms: 1.05x faster                                                     |
| gunicorn                | 1.13 ms                                                             | 1.07 ms: 1.05x faster                                                     |
| sqlglot_optimize        | 53.4 ms                                                             | 50.8 ms: 1.05x faster                                                     |
| bench_thread_pool       | 820 us                                                              | 781 us: 1.05x faster                                                      |
| sympy_expand            | 477 ms                                                              | 455 ms: 1.05x faster                                                      |
| logging_silent          | 98.7 ns                                                             | 94.2 ns: 1.05x faster                                                     |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                      |
| chaos                   | 68.0 ms                                                             | 65.0 ms: 1.05x faster                                                     |
| regex_compile           | 137 ms                                                              | 131 ms: 1.05x faster                                                      |
| coverage                | 101 ms                                                              | 96.8 ms: 1.04x faster                                                     |
| json                    | 4.86 ms                                                             | 4.65 ms: 1.04x faster                                                     |
| tornado_http            | 96.7 ms                                                             | 92.7 ms: 1.04x faster                                                     |
| chameleon               | 6.52 ms                                                             | 6.26 ms: 1.04x faster                                                     |
| pycparser               | 1.14 sec                                                            | 1.10 sec: 1.04x faster                                                    |
| sympy_str               | 291 ms                                                              | 280 ms: 1.04x faster                                                      |
| float                   | 76.0 ms                                                             | 73.1 ms: 1.04x faster                                                     |
| sympy_integrate         | 21.0 ms                                                             | 20.3 ms: 1.04x faster                                                     |
| logging_format          | 6.64 us                                                             | 6.41 us: 1.03x faster                                                     |
| meteor_contest          | 106 ms                                                              | 103 ms: 1.03x faster                                                      |
| sqlalchemy_imperative   | 18.0 ms                                                             | 17.4 ms: 1.03x faster                                                     |
| regex_v8                | 22.0 ms                                                             | 21.3 ms: 1.03x faster                                                     |
| comprehensions          | 22.2 us                                                             | 21.6 us: 1.03x faster                                                     |
| sympy_sum               | 167 ms                                                              | 162 ms: 1.03x faster                                                      |
| pprint_pformat          | 1.45 sec                                                            | 1.41 sec: 1.03x faster                                                    |
| sqlalchemy_declarative  | 138 ms                                                              | 135 ms: 1.03x faster                                                      |
| 2to3                    | 257 ms                                                              | 250 ms: 1.03x faster                                                      |
| genshi_text             | 21.8 ms                                                             | 21.3 ms: 1.03x faster                                                     |
| scimark_monte_carlo     | 67.8 ms                                                             | 66.0 ms: 1.03x faster                                                     |
| dulwich_log             | 63.6 ms                                                             | 62.0 ms: 1.03x faster                                                     |
| docutils                | 2.59 sec                                                            | 2.53 sec: 1.02x faster                                                    |
| scimark_lu              | 108 ms                                                              | 106 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed | 736 ms                                                              | 718 ms: 1.02x faster                                                      |
| go                      | 138 ms                                                              | 135 ms: 1.02x faster                                                      |
| telco                   | 6.59 ms                                                             | 6.44 ms: 1.02x faster                                                     |
| pprint_safe_repr        | 701 ms                                                              | 685 ms: 1.02x faster                                                      |
| async_tree_none         | 525 ms                                                              | 514 ms: 1.02x faster                                                      |
| deepcopy                | 339 us                                                              | 332 us: 1.02x faster                                                      |
| mdp                     | 2.64 sec                                                            | 2.60 sec: 1.02x faster                                                    |
| create_gc_cycles        | 1.48 ms                                                             | 1.47 ms: 1.01x faster                                                     |
| django_template         | 32.9 ms                                                             | 32.6 ms: 1.01x faster                                                     |
| deepcopy_reduce         | 2.96 us                                                             | 2.97 us: 1.01x slower                                                     |
| crypto_pyaes            | 73.8 ms                                                             | 74.5 ms: 1.01x slower                                                     |
| mako                    | 9.82 ms                                                             | 9.94 ms: 1.01x slower                                                     |
| xml_etree_process       | 54.1 ms                                                             | 55.8 ms: 1.03x slower                                                     |
| sqlite_synth            | 2.51 us                                                             | 2.60 us: 1.03x slower                                                     |
| thrift                  | 766 us                                                              | 791 us: 1.03x slower                                                      |
| python_startup          | 8.49 ms                                                             | 8.87 ms: 1.04x slower                                                     |
| pickle_list             | 4.03 us                                                             | 4.24 us: 1.05x slower                                                     |
| unpickle                | 13.2 us                                                             | 13.9 us: 1.05x slower                                                     |
| pickle_dict             | 30.9 us                                                             | 32.6 us: 1.05x slower                                                     |
| xml_etree_generate      | 76.5 ms                                                             | 80.7 ms: 1.05x slower                                                     |
| regex_dna               | 196 ms                                                              | 207 ms: 1.06x slower                                                      |
| regex_effbot            | 3.32 ms                                                             | 3.53 ms: 1.06x slower                                                     |
| python_startup_no_site  | 5.98 ms                                                             | 6.57 ms: 1.10x slower                                                     |
| pickle                  | 9.79 us                                                             | 10.9 us: 1.11x slower                                                     |
| gc_traversal            | 3.63 ms                                                             | 4.06 ms: 1.12x slower                                                     |
| async_generators        | 361 ms                                                              | 431 ms: 1.19x slower                                                      |
| dask                    | 368 ms                                                              | 487 ms: 1.32x slower                                                      |
| Geometric mean          | (ref)                                                               | 1.05x faster                                                              |

Benchmark hidden because not significant (7): djangocms, async_tree_memoization, fannkuch, pyflate, bench_mp_pool, async_tree_io, unpickle_list
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging
