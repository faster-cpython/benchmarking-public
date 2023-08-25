
# Results vs. 3.11.0

- fork: faster-cpython
- ref: restrict_for_iter_sp
- machine: linux-x86_64
- commit hash: fb5f321
- commit date: 2023-02-17
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 247 ms: 1.05x faster                                                             |
| chameleon      | 6.47 ms                                                | 6.39 ms: 1.01x faster                                                            |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                           |
| html5lib       | 64.5 ms                                                | 61.2 ms: 1.05x faster                                                            |
| tornado_http   | 96.3 ms                                                | 94.8 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.7 ms: 1.05x faster                                                            |
| pidigits       | 198 ms                                                 | 198 ms: 1.00x faster                                                             |
| nbody          | 93.1 ms                                                | 95.5 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.65 ms: 1.10x faster                                                            |
| regex_compile  | 138 ms                                                 | 132 ms: 1.04x faster                                                             |
| regex_dna      | 204 ms                                                 | 199 ms: 1.03x faster                                                             |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.50 ms: 1.32x faster                                                            |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                                             |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                                            |
| pickle_pure_python   | 306 us                                                 | 281 us: 1.09x faster                                                             |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                             |
| xml_etree_iterparse  | 104 ms                                                 | 99.7 ms: 1.04x faster                                                            |
| pickle_dict          | 31.1 us                                                | 30.2 us: 1.03x faster                                                            |
| pickle_list          | 4.11 us                                                | 4.01 us: 1.03x faster                                                            |
| pickle               | 10.1 us                                                | 9.98 us: 1.01x faster                                                            |
| unpickle_list        | 4.91 us                                                | 5.04 us: 1.03x slower                                                            |
| xml_etree_process    | 53.9 ms                                                | 55.7 ms: 1.03x slower                                                            |
| xml_etree_generate   | 76.2 ms                                                | 81.2 ms: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.92 ms: 1.05x slower                                                            |
| python_startup_no_site | 6.01 ms                                                | 6.47 ms: 1.08x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.4 ms: 1.07x faster                                                            |
| mako            | 10.1 ms                                                | 9.89 ms: 1.02x faster                                                            |
| genshi_text     | 21.6 ms                                                | 21.2 ms: 1.02x faster                                                            |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.6 ms: 2.40x faster                                                            |
| asyncio_tcp             | 922 ms                                                 | 504 ms: 1.83x faster                                                             |
| json_dumps              | 12.6 ms                                                | 9.50 ms: 1.32x faster                                                            |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                                             |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                                             |
| coroutines              | 25.5 ms                                                | 22.1 ms: 1.15x faster                                                            |
| deltablue               | 3.67 ms                                                | 3.19 ms: 1.15x faster                                                            |
| gc_traversal            | 4.02 ms                                                | 3.53 ms: 1.14x faster                                                            |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                                             |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                                            |
| regex_effbot            | 3.99 ms                                                | 3.65 ms: 1.10x faster                                                            |
| pickle_pure_python      | 306 us                                                 | 281 us: 1.09x faster                                                             |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                            |
| richards                | 45.7 ms                                                | 42.2 ms: 1.08x faster                                                            |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.08x faster                                                           |
| gunicorn                | 1.18 ms                                                | 1.10 ms: 1.07x faster                                                            |
| json                    | 4.94 ms                                                | 4.60 ms: 1.07x faster                                                            |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                                             |
| genshi_xml              | 51.8 ms                                                | 48.4 ms: 1.07x faster                                                            |
| deepcopy_memo           | 37.0 us                                                | 34.6 us: 1.07x faster                                                            |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                             |
| sympy_str               | 290 ms                                                 | 273 ms: 1.06x faster                                                             |
| spectral_norm           | 100 ms                                                 | 94.1 ms: 1.06x faster                                                            |
| logging_silent          | 101 ns                                                 | 95.7 ns: 1.06x faster                                                            |
| html5lib                | 64.5 ms                                                | 61.2 ms: 1.05x faster                                                            |
| logging_simple          | 6.03 us                                                | 5.74 us: 1.05x faster                                                            |
| logging_format          | 6.68 us                                                | 6.37 us: 1.05x faster                                                            |
| sympy_integrate         | 21.0 ms                                                | 20.0 ms: 1.05x faster                                                            |
| float                   | 77.2 ms                                                | 73.7 ms: 1.05x faster                                                            |
| 2to3                    | 259 ms                                                 | 247 ms: 1.05x faster                                                             |
| scimark_fft             | 328 ms                                                 | 314 ms: 1.05x faster                                                             |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                             |
| sympy_sum               | 167 ms                                                 | 159 ms: 1.04x faster                                                             |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                             |
| regex_compile           | 138 ms                                                 | 132 ms: 1.04x faster                                                             |
| xml_etree_iterparse     | 104 ms                                                 | 99.7 ms: 1.04x faster                                                            |
| pyflate                 | 418 ms                                                 | 402 ms: 1.04x faster                                                             |
| sqlglot_optimize        | 53.1 ms                                                | 51.1 ms: 1.04x faster                                                            |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                           |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.04x faster                                                           |
| bench_thread_pool       | 819 us                                                 | 791 us: 1.04x faster                                                             |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.03x faster                                                             |
| pprint_safe_repr        | 701 ms                                                 | 680 ms: 1.03x faster                                                             |
| pickle_dict             | 31.1 us                                                | 30.2 us: 1.03x faster                                                            |
| unpack_sequence         | 43.1 ns                                                | 41.9 ns: 1.03x faster                                                            |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                             |
| regex_dna               | 204 ms                                                 | 199 ms: 1.03x faster                                                             |
| deepcopy                | 342 us                                                 | 333 us: 1.03x faster                                                             |
| pickle_list             | 4.11 us                                                | 4.01 us: 1.03x faster                                                            |
| coverage                | 100 ms                                                 | 97.9 ms: 1.02x faster                                                            |
| raytrace                | 297 ms                                                 | 290 ms: 1.02x faster                                                             |
| nqueens                 | 83.4 ms                                                | 81.7 ms: 1.02x faster                                                            |
| mako                    | 10.1 ms                                                | 9.89 ms: 1.02x faster                                                            |
| genshi_text             | 21.6 ms                                                | 21.2 ms: 1.02x faster                                                            |
| chaos                   | 69.2 ms                                                | 68.0 ms: 1.02x faster                                                            |
| hexiom                  | 6.37 ms                                                | 6.27 ms: 1.02x faster                                                            |
| tornado_http            | 96.3 ms                                                | 94.8 ms: 1.02x faster                                                            |
| dulwich_log             | 63.7 ms                                                | 62.8 ms: 1.01x faster                                                            |
| scimark_monte_carlo     | 68.1 ms                                                | 67.1 ms: 1.01x faster                                                            |
| chameleon               | 6.47 ms                                                | 6.39 ms: 1.01x faster                                                            |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                                             |
| pickle                  | 10.1 us                                                | 9.98 us: 1.01x faster                                                            |
| regex_v8                | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                            |
| crypto_pyaes            | 74.7 ms                                                | 74.2 ms: 1.01x faster                                                            |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                                            |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                                            |
| pidigits                | 198 ms                                                 | 198 ms: 1.00x faster                                                             |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                            |
| sqlglot_transpile       | 1.70 ms                                                | 1.73 ms: 1.02x slower                                                            |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                           |
| thrift                  | 756 us                                                 | 769 us: 1.02x slower                                                             |
| mdp                     | 2.62 sec                                               | 2.66 sec: 1.02x slower                                                           |
| async_tree_cpu_io_mixed | 739 ms                                                 | 752 ms: 1.02x slower                                                             |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.60 ms: 1.02x slower                                                            |
| nbody                   | 93.1 ms                                                | 95.5 ms: 1.03x slower                                                            |
| unpickle_list           | 4.91 us                                                | 5.04 us: 1.03x slower                                                            |
| sqlglot_parse           | 1.40 ms                                                | 1.44 ms: 1.03x slower                                                            |
| xml_etree_process       | 53.9 ms                                                | 55.7 ms: 1.03x slower                                                            |
| python_startup          | 8.52 ms                                                | 8.92 ms: 1.05x slower                                                            |
| sqlite_synth            | 2.52 us                                                | 2.66 us: 1.05x slower                                                            |
| xml_etree_generate      | 76.2 ms                                                | 81.2 ms: 1.07x slower                                                            |
| python_startup_no_site  | 6.01 ms                                                | 6.47 ms: 1.08x slower                                                            |
| async_tree_memoization  | 627 ms                                                 | 677 ms: 1.08x slower                                                             |
| async_generators        | 368 ms                                                 | 410 ms: 1.11x slower                                                             |
| dask                    | 360 ms                                                 | 502 ms: 1.39x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (8): djangocms, bench_mp_pool, telco, deepcopy_reduce, scimark_lu, sqlalchemy_imperative, async_tree_none, unpickle
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
