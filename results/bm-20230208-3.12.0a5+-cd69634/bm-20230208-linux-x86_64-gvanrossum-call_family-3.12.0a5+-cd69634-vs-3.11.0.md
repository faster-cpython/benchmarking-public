
# Results vs. 3.11.0

- fork: gvanrossum
- ref: call_family
- machine: linux-x86_64
- commit hash: cd69634
- commit date: 2023-02-08
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                              |
| chameleon      | 6.47 ms                                                | 6.44 ms: 1.01x faster                                             |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                            |
| html5lib       | 64.5 ms                                                | 60.7 ms: 1.06x faster                                             |
| tornado_http   | 96.3 ms                                                | 94.3 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                              |
| float          | 77.2 ms                                                | 74.0 ms: 1.04x faster                                             |
| nbody          | 93.1 ms                                                | 94.6 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.64 ms: 1.10x faster                                             |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                              |
| regex_v8       | 22.0 ms                                                | 21.0 ms: 1.05x faster                                             |
| regex_dna      | 204 ms                                                 | 206 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.44 ms: 1.33x faster                                             |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.15x faster                                              |
| json_loads           | 26.5 us                                                | 23.8 us: 1.11x faster                                             |
| xml_etree_parse      | 158 ms                                                 | 146 ms: 1.09x faster                                              |
| pickle_pure_python   | 306 us                                                 | 286 us: 1.07x faster                                              |
| unpickle             | 13.7 us                                                | 13.0 us: 1.05x faster                                             |
| pickle_dict          | 31.1 us                                                | 30.3 us: 1.03x faster                                             |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                              |
| pickle_list          | 4.11 us                                                | 4.03 us: 1.02x faster                                             |
| xml_etree_process    | 53.9 ms                                                | 53.2 ms: 1.01x faster                                             |
| xml_etree_generate   | 76.2 ms                                                | 77.1 ms: 1.01x slower                                             |
| unpickle_list        | 4.91 us                                                | 4.97 us: 1.01x slower                                             |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                      |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.91 ms: 1.05x slower                                             |
| python_startup_no_site | 6.01 ms                                                | 6.47 ms: 1.08x slower                                             |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.1 ms: 1.10x faster                                             |
| genshi_text     | 21.6 ms                                                | 20.5 ms: 1.05x faster                                             |
| mako            | 10.1 ms                                                | 9.97 ms: 1.01x faster                                             |
| django_template | 32.6 ms                                                | 33.2 ms: 1.02x slower                                             |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 490 ms: 1.88x faster                                              |
| json_dumps              | 12.6 ms                                                | 9.44 ms: 1.33x faster                                             |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                              |
| deltablue               | 3.67 ms                                                | 3.17 ms: 1.16x faster                                             |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.15x faster                                              |
| scimark_sor             | 118 ms                                                 | 105 ms: 1.13x faster                                              |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.01 ms: 1.12x faster                                             |
| json_loads              | 26.5 us                                                | 23.8 us: 1.11x faster                                             |
| genshi_xml              | 51.8 ms                                                | 47.1 ms: 1.10x faster                                             |
| regex_effbot            | 3.99 ms                                                | 3.64 ms: 1.10x faster                                             |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.09x faster                                             |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                             |
| fannkuch                | 388 ms                                                 | 356 ms: 1.09x faster                                              |
| xml_etree_parse         | 158 ms                                                 | 146 ms: 1.09x faster                                              |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.08x faster                                            |
| richards                | 45.7 ms                                                | 42.3 ms: 1.08x faster                                             |
| scimark_fft             | 328 ms                                                 | 305 ms: 1.08x faster                                              |
| sympy_str               | 290 ms                                                 | 270 ms: 1.07x faster                                              |
| pickle_pure_python      | 306 us                                                 | 286 us: 1.07x faster                                              |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                              |
| sympy_sum               | 167 ms                                                 | 156 ms: 1.07x faster                                              |
| json                    | 4.94 ms                                                | 4.64 ms: 1.07x faster                                             |
| async_generators        | 368 ms                                                 | 346 ms: 1.06x faster                                              |
| html5lib                | 64.5 ms                                                | 60.7 ms: 1.06x faster                                             |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                             |
| deepcopy_memo           | 37.0 us                                                | 34.9 us: 1.06x faster                                             |
| hexiom                  | 6.37 ms                                                | 6.02 ms: 1.06x faster                                             |
| mdp                     | 2.62 sec                                               | 2.48 sec: 1.05x faster                                            |
| nqueens                 | 83.4 ms                                                | 79.2 ms: 1.05x faster                                             |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                            |
| regex_v8                | 22.0 ms                                                | 21.0 ms: 1.05x faster                                             |
| genshi_text             | 21.6 ms                                                | 20.5 ms: 1.05x faster                                             |
| logging_silent          | 101 ns                                                 | 96.3 ns: 1.05x faster                                             |
| unpickle                | 13.7 us                                                | 13.0 us: 1.05x faster                                             |
| coroutines              | 25.5 ms                                                | 24.3 ms: 1.05x faster                                             |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                              |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                              |
| bench_thread_pool       | 819 us                                                 | 783 us: 1.05x faster                                              |
| float                   | 77.2 ms                                                | 74.0 ms: 1.04x faster                                             |
| spectral_norm           | 100 ms                                                 | 96.1 ms: 1.04x faster                                             |
| chaos                   | 69.2 ms                                                | 66.7 ms: 1.04x faster                                             |
| logging_format          | 6.68 us                                                | 6.46 us: 1.04x faster                                             |
| telco                   | 6.58 ms                                                | 6.36 ms: 1.03x faster                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 65.8 ms: 1.03x faster                                             |
| sqlglot_optimize        | 53.1 ms                                                | 51.4 ms: 1.03x faster                                             |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                              |
| deepcopy                | 342 us                                                 | 332 us: 1.03x faster                                              |
| raytrace                | 297 ms                                                 | 288 ms: 1.03x faster                                              |
| pyflate                 | 418 ms                                                 | 407 ms: 1.03x faster                                              |
| logging_simple          | 6.03 us                                                | 5.88 us: 1.03x faster                                             |
| crypto_pyaes            | 74.7 ms                                                | 72.7 ms: 1.03x faster                                             |
| pickle_dict             | 31.1 us                                                | 30.3 us: 1.03x faster                                             |
| thrift                  | 756 us                                                 | 740 us: 1.02x faster                                              |
| tornado_http            | 96.3 ms                                                | 94.3 ms: 1.02x faster                                             |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                              |
| pickle_list             | 4.11 us                                                | 4.03 us: 1.02x faster                                             |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                            |
| generators              | 73.5 ms                                                | 72.1 ms: 1.02x faster                                             |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                              |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                             |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                              |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.01x faster                                              |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                             |
| coverage                | 100 ms                                                 | 98.8 ms: 1.01x faster                                             |
| xml_etree_process       | 53.9 ms                                                | 53.2 ms: 1.01x faster                                             |
| mako                    | 10.1 ms                                                | 9.97 ms: 1.01x faster                                             |
| pprint_safe_repr        | 701 ms                                                 | 697 ms: 1.01x faster                                              |
| chameleon               | 6.47 ms                                                | 6.44 ms: 1.01x faster                                             |
| deepcopy_reduce         | 2.94 us                                                | 2.96 us: 1.01x slower                                             |
| regex_dna               | 204 ms                                                 | 206 ms: 1.01x slower                                              |
| sqlalchemy_imperative   | 17.9 ms                                                | 18.1 ms: 1.01x slower                                             |
| xml_etree_generate      | 76.2 ms                                                | 77.1 ms: 1.01x slower                                             |
| unpickle_list           | 4.91 us                                                | 4.97 us: 1.01x slower                                             |
| nbody                   | 93.1 ms                                                | 94.6 ms: 1.02x slower                                             |
| django_template         | 32.6 ms                                                | 33.2 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed | 739 ms                                                 | 752 ms: 1.02x slower                                              |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                            |
| sqlglot_transpile       | 1.70 ms                                                | 1.74 ms: 1.02x slower                                             |
| sqlglot_parse           | 1.40 ms                                                | 1.44 ms: 1.03x slower                                             |
| unpack_sequence         | 43.1 ns                                                | 44.4 ns: 1.03x slower                                             |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                             |
| gc_traversal            | 4.02 ms                                                | 4.17 ms: 1.04x slower                                             |
| python_startup          | 8.52 ms                                                | 8.91 ms: 1.05x slower                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.47 ms: 1.08x slower                                             |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (8): djangocms, sqlalchemy_declarative, async_tree_none, dulwich_log, bench_mp_pool, meteor_contest, pickle, async_tree_memoization
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
