
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3adb23a
- commit date: 2023-03-18
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| chameleon      | 6.47 ms                                                | 6.35 ms: 1.02x faster                                  |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                 |
| html5lib       | 64.5 ms                                                | 61.2 ms: 1.05x faster                                  |
| tornado_http   | 96.3 ms                                                | 91.2 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 86.0 ms: 1.08x faster                                  |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| float          | 77.2 ms                                                | 73.9 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.63 ms: 1.10x faster                                  |
| regex_compile  | 138 ms                                                 | 135 ms: 1.03x faster                                   |
| regex_dna      | 204 ms                                                 | 201 ms: 1.01x faster                                   |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.57 ms: 1.31x faster                                  |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                   |
| json_loads           | 26.5 us                                                | 24.2 us: 1.10x faster                                  |
| pickle_pure_python   | 306 us                                                 | 284 us: 1.08x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle_dict          | 31.1 us                                                | 31.3 us: 1.00x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.00 us: 1.02x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 55.2 ms: 1.02x slower                                  |
| pickle_list          | 4.11 us                                                | 4.26 us: 1.04x slower                                  |
| pickle               | 10.1 us                                                | 10.4 us: 1.04x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 80.4 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.91 ms: 1.05x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.52 ms: 1.09x slower                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.1 ms: 1.10x faster                                  |
| genshi_text     | 21.6 ms                                                | 21.0 ms: 1.03x faster                                  |
| mako            | 10.1 ms                                                | 10.1 ms: 1.00x faster                                  |
| django_template | 32.6 ms                                                | 32.9 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.3 ms: 2.50x faster                                  |
| asyncio_tcp             | 922 ms                                                 | 507 ms: 1.82x faster                                   |
| json_dumps              | 12.6 ms                                                | 9.57 ms: 1.31x faster                                  |
| mypy2                   | 420 ms                                                 | 332 ms: 1.27x faster                                   |
| deltablue               | 3.67 ms                                                | 3.17 ms: 1.16x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                   |
| coroutines              | 25.5 ms                                                | 22.8 ms: 1.12x faster                                  |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                   |
| regex_effbot            | 3.99 ms                                                | 3.63 ms: 1.10x faster                                  |
| genshi_xml              | 51.8 ms                                                | 47.1 ms: 1.10x faster                                  |
| json_loads              | 26.5 us                                                | 24.2 us: 1.10x faster                                  |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                  |
| scimark_fft             | 328 ms                                                 | 300 ms: 1.09x faster                                   |
| richards                | 45.7 ms                                                | 41.9 ms: 1.09x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                  |
| nbody                   | 93.1 ms                                                | 86.0 ms: 1.08x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 34.2 us: 1.08x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.15 ms: 1.08x faster                                  |
| spectral_norm           | 100 ms                                                 | 92.7 ms: 1.08x faster                                  |
| pickle_pure_python      | 306 us                                                 | 284 us: 1.08x faster                                   |
| nqueens                 | 83.4 ms                                                | 77.9 ms: 1.07x faster                                  |
| json                    | 4.94 ms                                                | 4.62 ms: 1.07x faster                                  |
| logging_silent          | 101 ns                                                 | 94.9 ns: 1.07x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                   |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                 |
| logging_simple          | 6.03 us                                                | 5.69 us: 1.06x faster                                  |
| logging_format          | 6.68 us                                                | 6.31 us: 1.06x faster                                  |
| deepcopy                | 342 us                                                 | 323 us: 1.06x faster                                   |
| raytrace                | 297 ms                                                 | 280 ms: 1.06x faster                                   |
| tornado_http            | 96.3 ms                                                | 91.2 ms: 1.06x faster                                  |
| html5lib                | 64.5 ms                                                | 61.2 ms: 1.05x faster                                  |
| chaos                   | 69.2 ms                                                | 66.0 ms: 1.05x faster                                  |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| float                   | 77.2 ms                                                | 73.9 ms: 1.05x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                   |
| sqlglot_optimize        | 53.1 ms                                                | 50.9 ms: 1.04x faster                                  |
| bench_thread_pool       | 819 us                                                 | 785 us: 1.04x faster                                   |
| hexiom                  | 6.37 ms                                                | 6.11 ms: 1.04x faster                                  |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                 |
| sympy_expand            | 475 ms                                                 | 458 ms: 1.04x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 65.7 ms: 1.04x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                 |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.03x faster                                   |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                  |
| coverage                | 100 ms                                                 | 97.0 ms: 1.03x faster                                  |
| gc_traversal            | 4.02 ms                                                | 3.90 ms: 1.03x faster                                  |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                  |
| sympy_str               | 290 ms                                                 | 283 ms: 1.03x faster                                   |
| genshi_text             | 21.6 ms                                                | 21.0 ms: 1.03x faster                                  |
| regex_compile           | 138 ms                                                 | 135 ms: 1.03x faster                                   |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                   |
| telco                   | 6.58 ms                                                | 6.43 ms: 1.02x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pprint_safe_repr        | 701 ms                                                 | 686 ms: 1.02x faster                                   |
| chameleon               | 6.47 ms                                                | 6.35 ms: 1.02x faster                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                  |
| regex_dna               | 204 ms                                                 | 201 ms: 1.01x faster                                   |
| regex_v8                | 22.0 ms                                                | 21.7 ms: 1.01x faster                                  |
| crypto_pyaes            | 74.7 ms                                                | 73.7 ms: 1.01x faster                                  |
| dulwich_log             | 63.7 ms                                                | 63.0 ms: 1.01x faster                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                   |
| pyflate                 | 418 ms                                                 | 414 ms: 1.01x faster                                   |
| mako                    | 10.1 ms                                                | 10.1 ms: 1.00x faster                                  |
| mdp                     | 2.62 sec                                               | 2.61 sec: 1.00x faster                                 |
| pickle_dict             | 31.1 us                                                | 31.3 us: 1.00x slower                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.71 ms: 1.01x slower                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                  |
| django_template         | 32.6 ms                                                | 32.9 ms: 1.01x slower                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 747 ms: 1.01x slower                                   |
| unpickle_list           | 4.91 us                                                | 5.00 us: 1.02x slower                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                  |
| thrift                  | 756 us                                                 | 771 us: 1.02x slower                                   |
| xml_etree_process       | 53.9 ms                                                | 55.2 ms: 1.02x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 644 ms: 1.03x slower                                   |
| pickle_list             | 4.11 us                                                | 4.26 us: 1.04x slower                                  |
| pickle                  | 10.1 us                                                | 10.4 us: 1.04x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                  |
| python_startup          | 8.52 ms                                                | 8.91 ms: 1.05x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 80.4 ms: 1.06x slower                                  |
| comprehensions          | 22.4 us                                                | 23.8 us: 1.06x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.52 ms: 1.09x slower                                  |
| async_generators        | 368 ms                                                 | 413 ms: 1.12x slower                                   |
| dask                    | 360 ms                                                 | 501 ms: 1.39x slower                                   |
| Geometric mean          | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (9): unpickle, async_tree_none, sqlalchemy_imperative, scimark_lu, sympy_sum, async_tree_io, bench_mp_pool, unpack_sequence, djangocms
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
