
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 34ba834
- commit date: 2023-01-18
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 256 ms: 1.01x faster                                                       |
| chameleon      | 6.47 ms                                                | 6.56 ms: 1.01x slower                                                      |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                     |
| html5lib       | 64.5 ms                                                | 61.4 ms: 1.05x faster                                                      |
| tornado_http   | 96.3 ms                                                | 94.7 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 74.3 ms: 1.04x faster                                                      |
| nbody          | 93.1 ms                                                | 92.5 ms: 1.01x faster                                                      |
| pidigits       | 198 ms                                                 | 198 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.44 ms: 1.16x faster                                                      |
| regex_compile  | 138 ms                                                 | 130 ms: 1.06x faster                                                       |
| regex_v8       | 22.0 ms                                                | 21.1 ms: 1.04x faster                                                      |
| regex_dna      | 204 ms                                                 | 201 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.55 ms: 1.32x faster                                                      |
| unpickle_pure_python | 228 us                                                 | 209 us: 1.09x faster                                                       |
| json_loads           | 26.5 us                                                | 24.4 us: 1.09x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                       |
| pickle_pure_python   | 306 us                                                 | 290 us: 1.05x faster                                                       |
| unpickle             | 13.7 us                                                | 13.3 us: 1.03x faster                                                      |
| pickle_list          | 4.11 us                                                | 4.02 us: 1.02x faster                                                      |
| pickle_dict          | 31.1 us                                                | 30.6 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                       |
| xml_etree_process    | 53.9 ms                                                | 53.5 ms: 1.01x faster                                                      |
| xml_etree_generate   | 76.2 ms                                                | 77.2 ms: 1.01x slower                                                      |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.72 ms: 1.02x slower                                                      |
| python_startup_no_site | 6.01 ms                                                | 6.25 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 48.1 ms: 1.08x faster                                                      |
| mako           | 10.1 ms                                                | 9.57 ms: 1.05x faster                                                      |
| genshi_text    | 21.6 ms                                                | 20.5 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 491 ms: 1.88x faster                                                       |
| json_dumps              | 12.6 ms                                                | 9.55 ms: 1.32x faster                                                      |
| regex_effbot            | 3.99 ms                                                | 3.44 ms: 1.16x faster                                                      |
| deltablue               | 3.67 ms                                                | 3.32 ms: 1.11x faster                                                      |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                                      |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                                      |
| logging_silent          | 101 ns                                                 | 92.3 ns: 1.09x faster                                                      |
| unpickle_pure_python    | 228 us                                                 | 209 us: 1.09x faster                                                       |
| json_loads              | 26.5 us                                                | 24.4 us: 1.09x faster                                                      |
| deepcopy_memo           | 37.0 us                                                | 34.0 us: 1.09x faster                                                      |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.16 ms: 1.08x faster                                                      |
| genshi_xml              | 51.8 ms                                                | 48.1 ms: 1.08x faster                                                      |
| scimark_fft             | 328 ms                                                 | 305 ms: 1.08x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                       |
| sympy_str               | 290 ms                                                 | 271 ms: 1.07x faster                                                       |
| sympy_sum               | 167 ms                                                 | 156 ms: 1.07x faster                                                       |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.07x faster                                                     |
| regex_compile           | 138 ms                                                 | 130 ms: 1.06x faster                                                       |
| nqueens                 | 83.4 ms                                                | 78.7 ms: 1.06x faster                                                      |
| chaos                   | 69.2 ms                                                | 65.3 ms: 1.06x faster                                                      |
| json                    | 4.94 ms                                                | 4.67 ms: 1.06x faster                                                      |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                     |
| mako                    | 10.1 ms                                                | 9.57 ms: 1.05x faster                                                      |
| gc_traversal            | 4.02 ms                                                | 3.81 ms: 1.05x faster                                                      |
| pickle_pure_python      | 306 us                                                 | 290 us: 1.05x faster                                                       |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                                       |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                     |
| html5lib                | 64.5 ms                                                | 61.4 ms: 1.05x faster                                                      |
| genshi_text             | 21.6 ms                                                | 20.5 ms: 1.05x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 20.0 ms: 1.05x faster                                                      |
| spectral_norm           | 100 ms                                                 | 95.4 ms: 1.05x faster                                                      |
| richards                | 45.7 ms                                                | 43.8 ms: 1.04x faster                                                      |
| regex_v8                | 22.0 ms                                                | 21.1 ms: 1.04x faster                                                      |
| sqlglot_optimize        | 53.1 ms                                                | 50.8 ms: 1.04x faster                                                      |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                       |
| hexiom                  | 6.37 ms                                                | 6.12 ms: 1.04x faster                                                      |
| logging_format          | 6.68 us                                                | 6.42 us: 1.04x faster                                                      |
| float                   | 77.2 ms                                                | 74.3 ms: 1.04x faster                                                      |
| deepcopy                | 342 us                                                 | 329 us: 1.04x faster                                                       |
| pprint_safe_repr        | 701 ms                                                 | 677 ms: 1.04x faster                                                       |
| bench_thread_pool       | 819 us                                                 | 791 us: 1.04x faster                                                       |
| logging_simple          | 6.03 us                                                | 5.85 us: 1.03x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                       |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                       |
| unpickle                | 13.7 us                                                | 13.3 us: 1.03x faster                                                      |
| fannkuch                | 388 ms                                                 | 378 ms: 1.03x faster                                                       |
| async_generators        | 368 ms                                                 | 359 ms: 1.03x faster                                                       |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.03x faster                                                      |
| crypto_pyaes            | 74.7 ms                                                | 72.8 ms: 1.03x faster                                                      |
| create_gc_cycles        | 1.49 ms                                                | 1.45 ms: 1.02x faster                                                      |
| pickle_list             | 4.11 us                                                | 4.02 us: 1.02x faster                                                      |
| telco                   | 6.58 ms                                                | 6.44 ms: 1.02x faster                                                      |
| thrift                  | 756 us                                                 | 741 us: 1.02x faster                                                       |
| pickle_dict             | 31.1 us                                                | 30.6 us: 1.02x faster                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                       |
| tornado_http            | 96.3 ms                                                | 94.7 ms: 1.02x faster                                                      |
| regex_dna               | 204 ms                                                 | 201 ms: 1.02x faster                                                       |
| 2to3                    | 259 ms                                                 | 256 ms: 1.01x faster                                                       |
| dulwich_log             | 63.7 ms                                                | 62.9 ms: 1.01x faster                                                      |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                                       |
| xml_etree_process       | 53.9 ms                                                | 53.5 ms: 1.01x faster                                                      |
| scimark_monte_carlo     | 68.1 ms                                                | 67.6 ms: 1.01x faster                                                      |
| nbody                   | 93.1 ms                                                | 92.5 ms: 1.01x faster                                                      |
| mdp                     | 2.62 sec                                               | 2.60 sec: 1.01x faster                                                     |
| pidigits                | 198 ms                                                 | 198 ms: 1.00x faster                                                       |
| deepcopy_reduce         | 2.94 us                                                | 2.96 us: 1.01x slower                                                      |
| pyflate                 | 418 ms                                                 | 421 ms: 1.01x slower                                                       |
| coroutines              | 25.5 ms                                                | 25.8 ms: 1.01x slower                                                      |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                     |
| xml_etree_generate      | 76.2 ms                                                | 77.2 ms: 1.01x slower                                                      |
| chameleon               | 6.47 ms                                                | 6.56 ms: 1.01x slower                                                      |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                                       |
| unpickle_list           | 4.91 us                                                | 4.99 us: 1.02x slower                                                      |
| python_startup          | 8.52 ms                                                | 8.72 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed | 739 ms                                                 | 756 ms: 1.02x slower                                                       |
| scimark_sor             | 118 ms                                                 | 121 ms: 1.03x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.61 us: 1.04x slower                                                      |
| generators              | 73.5 ms                                                | 76.3 ms: 1.04x slower                                                      |
| python_startup_no_site  | 6.01 ms                                                | 6.25 ms: 1.04x slower                                                      |
| async_tree_memoization  | 627 ms                                                 | 659 ms: 1.05x slower                                                       |
| dask                    | 360 ms                                                 | 514 ms: 1.43x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (9): meteor_contest, pickle, sqlglot_transpile, djangocms, async_tree_none, bench_mp_pool, django_template, sqlglot_parse, unpack_sequence
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230118-3.12.0a4+-34ba834/bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
