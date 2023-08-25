
# Results vs. 3.11.0

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: ae0bd02
- commit date: 2023-02-13
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 245 ms: 1.06x faster                                          |
| chameleon      | 6.47 ms                                                | 6.44 ms: 1.01x faster                                         |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.03x faster                                        |
| html5lib       | 64.5 ms                                                | 60.8 ms: 1.06x faster                                         |
| tornado_http   | 96.3 ms                                                | 94.9 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.7 ms: 1.06x faster                                         |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                          |
| nbody          | 93.1 ms                                                | 99.9 ms: 1.07x slower                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.50 ms: 1.14x faster                                         |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                          |
| regex_dna      | 204 ms                                                 | 200 ms: 1.02x faster                                          |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.51 ms: 1.32x faster                                         |
| unpickle_pure_python | 228 us                                                 | 200 us: 1.14x faster                                          |
| json_loads           | 26.5 us                                                | 24.2 us: 1.10x faster                                         |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                          |
| pickle_pure_python   | 306 us                                                 | 286 us: 1.07x faster                                          |
| xml_etree_iterparse  | 104 ms                                                 | 99.8 ms: 1.04x faster                                         |
| unpickle             | 13.7 us                                                | 13.2 us: 1.04x faster                                         |
| pickle_dict          | 31.1 us                                                | 30.7 us: 1.01x faster                                         |
| xml_etree_process    | 53.9 ms                                                | 55.2 ms: 1.03x slower                                         |
| unpickle_list        | 4.91 us                                                | 5.04 us: 1.03x slower                                         |
| xml_etree_generate   | 76.2 ms                                                | 80.4 ms: 1.06x slower                                         |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                  |

Benchmark hidden because not significant (2): pickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.89 ms: 1.04x slower                                         |
| python_startup_no_site | 6.01 ms                                                | 6.45 ms: 1.07x slower                                         |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.8 ms: 1.11x faster                                         |
| genshi_text     | 21.6 ms                                                | 20.8 ms: 1.04x faster                                         |
| mako            | 10.1 ms                                                | 10.0 ms: 1.00x faster                                         |
| django_template | 32.6 ms                                                | 33.3 ms: 1.02x slower                                         |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.6 ms: 2.40x faster                                         |
| asyncio_tcp             | 922 ms                                                 | 502 ms: 1.84x faster                                          |
| json_dumps              | 12.6 ms                                                | 9.51 ms: 1.32x faster                                         |
| mypy2                   | 420 ms                                                 | 325 ms: 1.29x faster                                          |
| deltablue               | 3.67 ms                                                | 3.18 ms: 1.16x faster                                         |
| unpickle_pure_python    | 228 us                                                 | 200 us: 1.14x faster                                          |
| regex_effbot            | 3.99 ms                                                | 3.50 ms: 1.14x faster                                         |
| coroutines              | 25.5 ms                                                | 22.9 ms: 1.11x faster                                         |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.06 ms: 1.11x faster                                         |
| genshi_xml              | 51.8 ms                                                | 46.8 ms: 1.11x faster                                         |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                         |
| json_loads              | 26.5 us                                                | 24.2 us: 1.10x faster                                         |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.10x faster                                          |
| scimark_fft             | 328 ms                                                 | 300 ms: 1.09x faster                                          |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                         |
| sympy_str               | 290 ms                                                 | 268 ms: 1.08x faster                                          |
| sqlglot_normalize       | 108 ms                                                 | 99.7 ms: 1.08x faster                                         |
| logging_silent          | 101 ns                                                 | 93.8 ns: 1.08x faster                                         |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                          |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                          |
| spectral_norm           | 100 ms                                                 | 93.5 ms: 1.07x faster                                         |
| sympy_integrate         | 21.0 ms                                                | 19.6 ms: 1.07x faster                                         |
| pickle_pure_python      | 306 us                                                 | 286 us: 1.07x faster                                          |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.07x faster                                        |
| sympy_sum               | 167 ms                                                 | 156 ms: 1.07x faster                                          |
| sympy_expand            | 475 ms                                                 | 446 ms: 1.06x faster                                          |
| sqlglot_optimize        | 53.1 ms                                                | 49.9 ms: 1.06x faster                                         |
| float                   | 77.2 ms                                                | 72.7 ms: 1.06x faster                                         |
| html5lib                | 64.5 ms                                                | 60.8 ms: 1.06x faster                                         |
| chaos                   | 69.2 ms                                                | 65.2 ms: 1.06x faster                                         |
| richards                | 45.7 ms                                                | 43.1 ms: 1.06x faster                                         |
| deepcopy_memo           | 37.0 us                                                | 34.9 us: 1.06x faster                                         |
| 2to3                    | 259 ms                                                 | 245 ms: 1.06x faster                                          |
| logging_format          | 6.68 us                                                | 6.34 us: 1.05x faster                                         |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                        |
| nqueens                 | 83.4 ms                                                | 79.7 ms: 1.05x faster                                         |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                          |
| raytrace                | 297 ms                                                 | 284 ms: 1.05x faster                                          |
| hexiom                  | 6.37 ms                                                | 6.12 ms: 1.04x faster                                         |
| bench_thread_pool       | 819 us                                                 | 786 us: 1.04x faster                                          |
| xml_etree_iterparse     | 104 ms                                                 | 99.8 ms: 1.04x faster                                         |
| pyflate                 | 418 ms                                                 | 402 ms: 1.04x faster                                          |
| telco                   | 6.58 ms                                                | 6.33 ms: 1.04x faster                                         |
| scimark_monte_carlo     | 68.1 ms                                                | 65.5 ms: 1.04x faster                                         |
| unpickle                | 13.7 us                                                | 13.2 us: 1.04x faster                                         |
| async_tree_none         | 526 ms                                                 | 507 ms: 1.04x faster                                          |
| mdp                     | 2.62 sec                                               | 2.53 sec: 1.04x faster                                        |
| logging_simple          | 6.03 us                                                | 5.82 us: 1.04x faster                                         |
| genshi_text             | 21.6 ms                                                | 20.8 ms: 1.04x faster                                         |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.03x faster                                        |
| pprint_safe_repr        | 701 ms                                                 | 679 ms: 1.03x faster                                          |
| fannkuch                | 388 ms                                                 | 376 ms: 1.03x faster                                          |
| deepcopy                | 342 us                                                 | 332 us: 1.03x faster                                          |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.4 ms: 1.03x faster                                         |
| create_gc_cycles        | 1.49 ms                                                | 1.44 ms: 1.03x faster                                         |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                          |
| sqlalchemy_declarative  | 138 ms                                                 | 135 ms: 1.02x faster                                          |
| regex_dna               | 204 ms                                                 | 200 ms: 1.02x faster                                          |
| async_tree_memoization  | 627 ms                                                 | 615 ms: 1.02x faster                                          |
| json                    | 4.94 ms                                                | 4.85 ms: 1.02x faster                                         |
| coverage                | 100 ms                                                 | 98.2 ms: 1.02x faster                                         |
| async_tree_io           | 1.30 sec                                               | 1.27 sec: 1.02x faster                                        |
| crypto_pyaes            | 74.7 ms                                                | 73.4 ms: 1.02x faster                                         |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                         |
| tornado_http            | 96.3 ms                                                | 94.9 ms: 1.01x faster                                         |
| pickle_dict             | 31.1 us                                                | 30.7 us: 1.01x faster                                         |
| dulwich_log             | 63.7 ms                                                | 62.9 ms: 1.01x faster                                         |
| scimark_lu              | 110 ms                                                 | 109 ms: 1.01x faster                                          |
| regex_v8                | 22.0 ms                                                | 21.9 ms: 1.01x faster                                         |
| chameleon               | 6.47 ms                                                | 6.44 ms: 1.01x faster                                         |
| mako                    | 10.1 ms                                                | 10.0 ms: 1.00x faster                                         |
| go                      | 140 ms                                                 | 139 ms: 1.00x faster                                          |
| gc_traversal            | 4.02 ms                                                | 4.04 ms: 1.00x slower                                         |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                         |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.02x slower                                         |
| django_template         | 32.6 ms                                                | 33.3 ms: 1.02x slower                                         |
| xml_etree_process       | 53.9 ms                                                | 55.2 ms: 1.03x slower                                         |
| unpickle_list           | 4.91 us                                                | 5.04 us: 1.03x slower                                         |
| deepcopy_reduce         | 2.94 us                                                | 3.03 us: 1.03x slower                                         |
| sqlite_synth            | 2.52 us                                                | 2.63 us: 1.04x slower                                         |
| python_startup          | 8.52 ms                                                | 8.89 ms: 1.04x slower                                         |
| unpack_sequence         | 43.1 ns                                                | 45.5 ns: 1.06x slower                                         |
| xml_etree_generate      | 76.2 ms                                                | 80.4 ms: 1.06x slower                                         |
| nbody                   | 93.1 ms                                                | 99.9 ms: 1.07x slower                                         |
| python_startup_no_site  | 6.01 ms                                                | 6.45 ms: 1.07x slower                                         |
| async_generators        | 368 ms                                                 | 414 ms: 1.12x slower                                          |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                  |

Benchmark hidden because not significant (6): thrift, pickle, bench_mp_pool, pickle_list, djangocms, async_tree_cpu_io_mixed
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
