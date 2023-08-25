
# Results vs. 3.11.0

- fork: gaogaotiantian
- ref: pep669_cprofile
- machine: linux-x86_64
- commit hash: 20f4663
- commit date: 2023-04-19
- overall geometric mean: 1.06x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                                      |
| chameleon      | 6.47 ms                                                | 6.26 ms: 1.03x faster                                                     |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                    |
| html5lib       | 64.5 ms                                                | 60.6 ms: 1.07x faster                                                     |
| tornado_http   | 96.3 ms                                                | 92.7 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 85.1 ms: 1.09x faster                                                     |
| float          | 77.2 ms                                                | 73.1 ms: 1.06x faster                                                     |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.53 ms: 1.13x faster                                                     |
| regex_compile  | 138 ms                                                 | 131 ms: 1.06x faster                                                      |
| regex_v8       | 22.0 ms                                                | 21.3 ms: 1.03x faster                                                     |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.37 ms: 1.34x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 201 us: 1.14x faster                                                      |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 283 us: 1.08x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 98.8 ms: 1.05x faster                                                     |
| unpickle_list        | 4.91 us                                                | 4.97 us: 1.01x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.24 us: 1.03x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 55.8 ms: 1.04x slower                                                     |
| pickle_dict          | 31.1 us                                                | 32.6 us: 1.05x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 80.7 ms: 1.06x slower                                                     |
| pickle               | 10.1 us                                                | 10.9 us: 1.08x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.87 ms: 1.04x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.57 ms: 1.09x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 46.2 ms: 1.12x faster                                                     |
| mako           | 10.1 ms                                                | 9.94 ms: 1.01x faster                                                     |
| genshi_text    | 21.6 ms                                                | 21.3 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 28.3 ms: 2.60x faster                                                     |
| asyncio_tcp             | 922 ms                                                 | 500 ms: 1.84x faster                                                      |
| json_dumps              | 12.6 ms                                                | 9.37 ms: 1.34x faster                                                     |
| mypy2                   | 420 ms                                                 | 329 ms: 1.28x faster                                                      |
| sqlglot_parse           | 1.40 ms                                                | 1.20 ms: 1.17x faster                                                     |
| deltablue               | 3.67 ms                                                | 3.19 ms: 1.15x faster                                                     |
| coroutines              | 25.5 ms                                                | 22.1 ms: 1.15x faster                                                     |
| sqlglot_transpile       | 1.70 ms                                                | 1.49 ms: 1.14x faster                                                     |
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.14x faster                                                      |
| regex_effbot            | 3.99 ms                                                | 3.53 ms: 1.13x faster                                                     |
| genshi_xml              | 51.8 ms                                                | 46.2 ms: 1.12x faster                                                     |
| richards                | 45.7 ms                                                | 41.3 ms: 1.11x faster                                                     |
| aiohttp                 | 1.10 ms                                                | 998 us: 1.10x faster                                                      |
| spectral_norm           | 100 ms                                                 | 90.9 ms: 1.10x faster                                                     |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                                     |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                                     |
| scimark_fft             | 328 ms                                                 | 300 ms: 1.09x faster                                                      |
| nbody                   | 93.1 ms                                                | 85.1 ms: 1.09x faster                                                     |
| scimark_sor             | 118 ms                                                 | 109 ms: 1.09x faster                                                      |
| deepcopy_memo           | 37.0 us                                                | 34.2 us: 1.08x faster                                                     |
| pickle_pure_python      | 306 us                                                 | 283 us: 1.08x faster                                                      |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                      |
| raytrace                | 297 ms                                                 | 276 ms: 1.08x faster                                                      |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.07x faster                                                    |
| logging_silent          | 101 ns                                                 | 94.2 ns: 1.07x faster                                                     |
| pathlib                 | 18.2 ms                                                | 17.0 ms: 1.07x faster                                                     |
| hexiom                  | 6.37 ms                                                | 5.96 ms: 1.07x faster                                                     |
| pylint                  | 465 ms                                                 | 435 ms: 1.07x faster                                                      |
| html5lib                | 64.5 ms                                                | 60.6 ms: 1.07x faster                                                     |
| chaos                   | 69.2 ms                                                | 65.0 ms: 1.06x faster                                                     |
| json                    | 4.94 ms                                                | 4.65 ms: 1.06x faster                                                     |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.25 ms: 1.06x faster                                                     |
| float                   | 77.2 ms                                                | 73.1 ms: 1.06x faster                                                     |
| regex_compile           | 138 ms                                                 | 131 ms: 1.06x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 102 ms: 1.05x faster                                                      |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 98.8 ms: 1.05x faster                                                     |
| logging_simple          | 6.03 us                                                | 5.74 us: 1.05x faster                                                     |
| nqueens                 | 83.4 ms                                                | 79.5 ms: 1.05x faster                                                     |
| bench_thread_pool       | 819 us                                                 | 781 us: 1.05x faster                                                      |
| sqlglot_optimize        | 53.1 ms                                                | 50.8 ms: 1.04x faster                                                     |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                      |
| logging_format          | 6.68 us                                                | 6.41 us: 1.04x faster                                                     |
| comprehensions          | 22.4 us                                                | 21.6 us: 1.04x faster                                                     |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                    |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                                      |
| tornado_http            | 96.3 ms                                                | 92.7 ms: 1.04x faster                                                     |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.04x faster                                                      |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.04x faster                                                     |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                      |
| sympy_str               | 290 ms                                                 | 280 ms: 1.04x faster                                                      |
| regex_v8                | 22.0 ms                                                | 21.3 ms: 1.03x faster                                                     |
| chameleon               | 6.47 ms                                                | 6.26 ms: 1.03x faster                                                     |
| coverage                | 100 ms                                                 | 96.8 ms: 1.03x faster                                                     |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                    |
| scimark_monte_carlo     | 68.1 ms                                                | 66.0 ms: 1.03x faster                                                     |
| deepcopy                | 342 us                                                 | 332 us: 1.03x faster                                                      |
| async_tree_cpu_io_mixed | 739 ms                                                 | 718 ms: 1.03x faster                                                      |
| dulwich_log             | 63.7 ms                                                | 62.0 ms: 1.03x faster                                                     |
| sqlalchemy_declarative  | 138 ms                                                 | 135 ms: 1.03x faster                                                      |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.4 ms: 1.03x faster                                                     |
| sympy_sum               | 167 ms                                                 | 162 ms: 1.02x faster                                                      |
| async_tree_none         | 526 ms                                                 | 514 ms: 1.02x faster                                                      |
| pprint_safe_repr        | 701 ms                                                 | 685 ms: 1.02x faster                                                      |
| telco                   | 6.58 ms                                                | 6.44 ms: 1.02x faster                                                     |
| async_tree_memoization  | 627 ms                                                 | 616 ms: 1.02x faster                                                      |
| mako                    | 10.1 ms                                                | 9.94 ms: 1.01x faster                                                     |
| genshi_text             | 21.6 ms                                                | 21.3 ms: 1.01x faster                                                     |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                     |
| fannkuch                | 388 ms                                                 | 383 ms: 1.01x faster                                                      |
| pyflate                 | 418 ms                                                 | 413 ms: 1.01x faster                                                      |
| async_tree_io           | 1.30 sec                                               | 1.28 sec: 1.01x faster                                                    |
| mdp                     | 2.62 sec                                               | 2.60 sec: 1.01x faster                                                    |
| crypto_pyaes            | 74.7 ms                                                | 74.5 ms: 1.00x faster                                                     |
| gc_traversal            | 4.02 ms                                                | 4.06 ms: 1.01x slower                                                     |
| deepcopy_reduce         | 2.94 us                                                | 2.97 us: 1.01x slower                                                     |
| unpickle_list           | 4.91 us                                                | 4.97 us: 1.01x slower                                                     |
| regex_dna               | 204 ms                                                 | 207 ms: 1.02x slower                                                      |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                                     |
| pickle_list             | 4.11 us                                                | 4.24 us: 1.03x slower                                                     |
| xml_etree_process       | 53.9 ms                                                | 55.8 ms: 1.04x slower                                                     |
| python_startup          | 8.52 ms                                                | 8.87 ms: 1.04x slower                                                     |
| thrift                  | 756 us                                                 | 791 us: 1.05x slower                                                      |
| pickle_dict             | 31.1 us                                                | 32.6 us: 1.05x slower                                                     |
| xml_etree_generate      | 76.2 ms                                                | 80.7 ms: 1.06x slower                                                     |
| pickle                  | 10.1 us                                                | 10.9 us: 1.08x slower                                                     |
| python_startup_no_site  | 6.01 ms                                                | 6.57 ms: 1.09x slower                                                     |
| async_generators        | 368 ms                                                 | 431 ms: 1.17x slower                                                      |
| dask                    | 360 ms                                                 | 487 ms: 1.35x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.06x faster                                                              |

Benchmark hidden because not significant (5): djangocms, unpack_sequence, bench_mp_pool, django_template, unpickle
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
