
# Results vs. 3.11.0

- fork: itamaro
- ref: eager_tasks_factory
- machine: linux-x86_64
- commit hash: bcf40dc
- commit date: 2023-03-20
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.27 ms: 1.03x faster                                                  |
| docutils       | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                 |
| html5lib       | 64.5 ms                                                | 60.6 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.6 ms: 1.06x faster                                                  |
| float          | 77.2 ms                                                | 74.0 ms: 1.04x faster                                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.30 ms: 1.21x faster                                                  |
| regex_compile  | 138 ms                                                 | 132 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.51 ms: 1.32x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                                   |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 281 us: 1.09x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| pickle_dict          | 31.1 us                                                | 31.3 us: 1.00x slower                                                  |
| unpickle_list        | 4.91 us                                                | 4.97 us: 1.01x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.21 us: 1.02x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 55.3 ms: 1.03x slower                                                  |
| pickle               | 10.1 us                                                | 10.4 us: 1.04x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 80.1 ms: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.96 ms: 1.05x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.55 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.8 ms: 1.08x faster                                                  |
| genshi_text     | 21.6 ms                                                | 21.0 ms: 1.03x faster                                                  |
| mako            | 10.1 ms                                                | 9.99 ms: 1.01x faster                                                  |
| django_template | 32.6 ms                                                | 33.2 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.4 ms: 2.50x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 506 ms: 1.82x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.51 ms: 1.32x faster                                                  |
| mypy2                   | 420 ms                                                 | 332 ms: 1.26x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.30 ms: 1.21x faster                                                  |
| deltablue               | 3.67 ms                                                | 3.14 ms: 1.17x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                                   |
| coroutines              | 25.5 ms                                                | 22.4 ms: 1.14x faster                                                  |
| spectral_norm           | 100 ms                                                 | 88.2 ms: 1.13x faster                                                  |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.11x faster                                                   |
| scimark_fft             | 328 ms                                                 | 297 ms: 1.10x faster                                                   |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                                  |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                  |
| deepcopy_memo           | 37.0 us                                                | 34.0 us: 1.09x faster                                                  |
| richards                | 45.7 ms                                                | 42.0 ms: 1.09x faster                                                  |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                  |
| pickle_pure_python      | 306 us                                                 | 281 us: 1.09x faster                                                   |
| genshi_xml              | 51.8 ms                                                | 47.8 ms: 1.08x faster                                                  |
| json                    | 4.94 ms                                                | 4.59 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.18 ms: 1.07x faster                                                  |
| logging_format          | 6.68 us                                                | 6.23 us: 1.07x faster                                                  |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                   |
| nqueens                 | 83.4 ms                                                | 78.2 ms: 1.07x faster                                                  |
| html5lib                | 64.5 ms                                                | 60.6 ms: 1.06x faster                                                  |
| nbody                   | 93.1 ms                                                | 87.6 ms: 1.06x faster                                                  |
| fannkuch                | 388 ms                                                 | 365 ms: 1.06x faster                                                   |
| deepcopy                | 342 us                                                 | 323 us: 1.06x faster                                                   |
| logging_simple          | 6.03 us                                                | 5.69 us: 1.06x faster                                                  |
| chaos                   | 69.2 ms                                                | 65.5 ms: 1.06x faster                                                  |
| pycparser               | 1.18 sec                                               | 1.12 sec: 1.06x faster                                                 |
| logging_silent          | 101 ns                                                 | 96.2 ns: 1.05x faster                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 50.6 ms: 1.05x faster                                                  |
| hexiom                  | 6.37 ms                                                | 6.08 ms: 1.05x faster                                                  |
| bench_thread_pool       | 819 us                                                 | 783 us: 1.05x faster                                                   |
| regex_compile           | 138 ms                                                 | 132 ms: 1.05x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| float                   | 77.2 ms                                                | 74.0 ms: 1.04x faster                                                  |
| raytrace                | 297 ms                                                 | 284 ms: 1.04x faster                                                   |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                   |
| docutils                | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                 |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 65.5 ms: 1.04x faster                                                  |
| pyflate                 | 418 ms                                                 | 403 ms: 1.04x faster                                                   |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                 |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                   |
| telco                   | 6.58 ms                                                | 6.36 ms: 1.04x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                  |
| coverage                | 100 ms                                                 | 96.8 ms: 1.03x faster                                                  |
| sympy_str               | 290 ms                                                 | 281 ms: 1.03x faster                                                   |
| chameleon               | 6.47 ms                                                | 6.27 ms: 1.03x faster                                                  |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                  |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                   |
| genshi_text             | 21.6 ms                                                | 21.0 ms: 1.03x faster                                                  |
| mdp                     | 2.62 sec                                               | 2.55 sec: 1.02x faster                                                 |
| pprint_safe_repr        | 701 ms                                                 | 687 ms: 1.02x faster                                                   |
| crypto_pyaes            | 74.7 ms                                                | 73.2 ms: 1.02x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                   |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.6 ms: 1.02x faster                                                  |
| dulwich_log             | 63.7 ms                                                | 62.9 ms: 1.01x faster                                                  |
| async_tree_none         | 526 ms                                                 | 521 ms: 1.01x faster                                                   |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                                   |
| gc_traversal            | 4.02 ms                                                | 3.98 ms: 1.01x faster                                                  |
| mako                    | 10.1 ms                                                | 9.99 ms: 1.01x faster                                                  |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                   |
| pickle_dict             | 31.1 us                                                | 31.3 us: 1.00x slower                                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.49 ms: 1.01x slower                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.01x slower                                                  |
| unpickle_list           | 4.91 us                                                | 4.97 us: 1.01x slower                                                  |
| django_template         | 32.6 ms                                                | 33.2 ms: 1.02x slower                                                  |
| pickle_list             | 4.11 us                                                | 4.21 us: 1.02x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.03x slower                                                  |
| xml_etree_process       | 53.9 ms                                                | 55.3 ms: 1.03x slower                                                  |
| pickle                  | 10.1 us                                                | 10.4 us: 1.04x slower                                                  |
| thrift                  | 756 us                                                 | 788 us: 1.04x slower                                                   |
| comprehensions          | 22.4 us                                                | 23.4 us: 1.04x slower                                                  |
| xml_etree_generate      | 76.2 ms                                                | 80.1 ms: 1.05x slower                                                  |
| python_startup          | 8.52 ms                                                | 8.96 ms: 1.05x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.55 ms: 1.09x slower                                                  |
| async_generators        | 368 ms                                                 | 411 ms: 1.12x slower                                                   |
| dask                    | 360 ms                                                 | 499 ms: 1.39x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (12): unpickle, async_tree_memoization, meteor_contest, djangocms, async_tree_io, unpack_sequence, async_tree_cpu_io_mixed, bench_mp_pool, deepcopy_reduce, regex_dna, sqlglot_transpile, regex_v8
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
