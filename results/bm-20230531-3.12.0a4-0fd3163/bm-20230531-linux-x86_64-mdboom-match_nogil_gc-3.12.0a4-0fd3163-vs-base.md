
# Results vs. base

- fork: mdboom
- ref: match_nogil_gc
- machine: linux-x86_64
- commit hash: 0fd3163
- commit date: 2023-05-31
- overall geometric mean: 1.04x faster \*
- HPT reliability: 99.54%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 253 ms                                                                | 245 ms: 1.03x faster                                            |
| chameleon      | 6.46 ms                                                               | 6.37 ms: 1.02x faster                                           |
| docutils       | 2.48 sec                                                              | 2.15 sec: 1.15x faster                                          |
| html5lib       | 59.8 ms                                                               | 57.8 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 72.2 ms                                                               | 60.7 ms: 1.19x faster                                           |
| pidigits       | 192 ms                                                                | 189 ms: 1.02x faster                                            |
| nbody          | 93.1 ms                                                               | 92.3 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.49 ms                                                               | 3.46 ms: 1.01x faster                                           |
| regex_dna      | 209 ms                                                                | 210 ms: 1.01x slower                                            |
| regex_v8       | 21.1 ms                                                               | 22.1 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_iterparse  | 106 ms                                                                | 80.9 ms: 1.32x faster                                           |
| xml_etree_parse      | 149 ms                                                                | 122 ms: 1.22x faster                                            |
| xml_etree_generate   | 77.5 ms                                                               | 73.4 ms: 1.06x faster                                           |
| xml_etree_process    | 53.9 ms                                                               | 51.6 ms: 1.04x faster                                           |
| json_loads           | 24.3 us                                                               | 23.7 us: 1.03x faster                                           |
| pickle_pure_python   | 285 us                                                                | 282 us: 1.01x faster                                            |
| unpickle_pure_python | 200 us                                                                | 198 us: 1.01x faster                                            |
| unpickle             | 13.0 us                                                               | 13.0 us: 1.01x slower                                           |
| pickle_list          | 4.02 us                                                               | 4.05 us: 1.01x slower                                           |
| pickle               | 10.0 us                                                               | 10.2 us: 1.02x slower                                           |
| pickle_dict          | 30.0 us                                                               | 31.2 us: 1.04x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.04x faster                                                    |

Benchmark hidden because not significant (2): unpickle_list, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 8.54 ms                                                               | 8.24 ms: 1.04x faster                                           |
| python_startup_no_site | 6.09 ms                                                               | 5.93 ms: 1.03x faster                                           |
| Geometric mean         | (ref)                                                                 | 1.03x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text     | 20.8 ms                                                               | 20.2 ms: 1.03x faster                                           |
| genshi_xml      | 46.5 ms                                                               | 45.9 ms: 1.01x faster                                           |
| mako            | 9.74 ms                                                               | 9.69 ms: 1.00x faster                                           |
| django_template | 32.6 ms                                                               | 32.9 ms: 1.01x slower                                           |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                    |

All benchmarks:
===============

| Benchmark               | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io           | 1.30 sec                                                              | 534 ms: 2.43x faster                                            |
| async_tree_none         | 521 ms                                                                | 260 ms: 2.00x faster                                            |
| async_tree_memoization  | 616 ms                                                                | 315 ms: 1.95x faster                                            |
| async_tree_cpu_io_mixed | 747 ms                                                                | 469 ms: 1.59x faster                                            |
| xml_etree_iterparse     | 106 ms                                                                | 80.9 ms: 1.32x faster                                           |
| xml_etree_parse         | 149 ms                                                                | 122 ms: 1.22x faster                                            |
| float                   | 72.2 ms                                                               | 60.7 ms: 1.19x faster                                           |
| docutils                | 2.48 sec                                                              | 2.15 sec: 1.15x faster                                          |
| dask                    | 355 ms                                                                | 317 ms: 1.12x faster                                            |
| mdp                     | 2.66 sec                                                              | 2.48 sec: 1.07x faster                                          |
| mypy2                   | 332 ms                                                                | 309 ms: 1.07x faster                                            |
| gc_traversal            | 3.57 ms                                                               | 3.38 ms: 1.06x faster                                           |
| xml_etree_generate      | 77.5 ms                                                               | 73.4 ms: 1.06x faster                                           |
| async_generators        | 354 ms                                                                | 338 ms: 1.05x faster                                            |
| deltablue               | 3.25 ms                                                               | 3.11 ms: 1.04x faster                                           |
| xml_etree_process       | 53.9 ms                                                               | 51.6 ms: 1.04x faster                                           |
| logging_silent          | 93.5 ns                                                               | 89.6 ns: 1.04x faster                                           |
| python_startup          | 8.54 ms                                                               | 8.24 ms: 1.04x faster                                           |
| html5lib                | 59.8 ms                                                               | 57.8 ms: 1.04x faster                                           |
| json                    | 4.74 ms                                                               | 4.59 ms: 1.03x faster                                           |
| genshi_text             | 20.8 ms                                                               | 20.2 ms: 1.03x faster                                           |
| 2to3                    | 253 ms                                                                | 245 ms: 1.03x faster                                            |
| python_startup_no_site  | 6.09 ms                                                               | 5.93 ms: 1.03x faster                                           |
| crypto_pyaes            | 75.7 ms                                                               | 73.7 ms: 1.03x faster                                           |
| json_loads              | 24.3 us                                                               | 23.7 us: 1.03x faster                                           |
| deepcopy_memo           | 34.7 us                                                               | 33.8 us: 1.03x faster                                           |
| pycparser               | 1.08 sec                                                              | 1.06 sec: 1.02x faster                                          |
| deepcopy                | 339 us                                                                | 332 us: 1.02x faster                                            |
| sqlglot_parse           | 1.41 ms                                                               | 1.38 ms: 1.02x faster                                           |
| scimark_lu              | 107 ms                                                                | 105 ms: 1.02x faster                                            |
| scimark_sor             | 108 ms                                                                | 106 ms: 1.02x faster                                            |
| pidigits                | 192 ms                                                                | 189 ms: 1.02x faster                                            |
| sqlglot_transpile       | 1.69 ms                                                               | 1.67 ms: 1.02x faster                                           |
| scimark_fft             | 314 ms                                                                | 309 ms: 1.02x faster                                            |
| chameleon               | 6.46 ms                                                               | 6.37 ms: 1.02x faster                                           |
| genshi_xml              | 46.5 ms                                                               | 45.9 ms: 1.01x faster                                           |
| pickle_pure_python      | 285 us                                                                | 282 us: 1.01x faster                                            |
| regex_effbot            | 3.49 ms                                                               | 3.46 ms: 1.01x faster                                           |
| unpickle_pure_python    | 200 us                                                                | 198 us: 1.01x faster                                            |
| nbody                   | 93.1 ms                                                               | 92.3 ms: 1.01x faster                                           |
| scimark_monte_carlo     | 65.7 ms                                                               | 65.2 ms: 1.01x faster                                           |
| deepcopy_reduce         | 2.99 us                                                               | 2.97 us: 1.01x faster                                           |
| sympy_integrate         | 20.3 ms                                                               | 20.2 ms: 1.01x faster                                           |
| pprint_safe_repr        | 680 ms                                                                | 676 ms: 1.01x faster                                            |
| nqueens                 | 78.0 ms                                                               | 77.6 ms: 1.01x faster                                           |
| sympy_str               | 282 ms                                                                | 281 ms: 1.00x faster                                            |
| mako                    | 9.74 ms                                                               | 9.69 ms: 1.00x faster                                           |
| logging_simple          | 5.77 us                                                               | 5.80 us: 1.01x slower                                           |
| unpickle                | 13.0 us                                                               | 13.0 us: 1.01x slower                                           |
| create_gc_cycles        | 1.45 ms                                                               | 1.46 ms: 1.01x slower                                           |
| pathlib                 | 18.0 ms                                                               | 18.2 ms: 1.01x slower                                           |
| comprehensions          | 23.7 us                                                               | 23.9 us: 1.01x slower                                           |
| pickle_list             | 4.02 us                                                               | 4.05 us: 1.01x slower                                           |
| regex_dna               | 209 ms                                                                | 210 ms: 1.01x slower                                            |
| pprint_pformat          | 1.38 sec                                                              | 1.39 sec: 1.01x slower                                          |
| raytrace                | 284 ms                                                                | 286 ms: 1.01x slower                                            |
| django_template         | 32.6 ms                                                               | 32.9 ms: 1.01x slower                                           |
| logging_format          | 6.35 us                                                               | 6.44 us: 1.01x slower                                           |
| bench_thread_pool       | 782 us                                                                | 792 us: 1.01x slower                                            |
| asyncio_tcp             | 504 ms                                                                | 511 ms: 1.01x slower                                            |
| hexiom                  | 5.98 ms                                                               | 6.06 ms: 1.01x slower                                           |
| go                      | 135 ms                                                                | 137 ms: 1.02x slower                                            |
| pickle                  | 10.0 us                                                               | 10.2 us: 1.02x slower                                           |
| pyflate                 | 397 ms                                                                | 403 ms: 1.02x slower                                            |
| chaos                   | 67.7 ms                                                               | 68.8 ms: 1.02x slower                                           |
| fannkuch                | 362 ms                                                                | 368 ms: 1.02x slower                                            |
| sqlglot_optimize        | 50.7 ms                                                               | 51.6 ms: 1.02x slower                                           |
| dulwich_log             | 62.1 ms                                                               | 63.5 ms: 1.02x slower                                           |
| coroutines              | 25.4 ms                                                               | 26.1 ms: 1.02x slower                                           |
| thrift                  | 752 us                                                                | 772 us: 1.03x slower                                            |
| sqlglot_normalize       | 104 ms                                                                | 108 ms: 1.04x slower                                            |
| sqlite_synth            | 2.57 us                                                               | 2.67 us: 1.04x slower                                           |
| telco                   | 6.26 ms                                                               | 6.52 ms: 1.04x slower                                           |
| pickle_dict             | 30.0 us                                                               | 31.2 us: 1.04x slower                                           |
| meteor_contest          | 104 ms                                                                | 109 ms: 1.05x slower                                            |
| regex_v8                | 21.1 ms                                                               | 22.1 ms: 1.05x slower                                           |
| unpack_sequence         | 41.4 ns                                                               | 43.6 ns: 1.05x slower                                           |
| djangocms               | 30.9 us                                                               | 33.1 us: 1.07x slower                                           |
| Geometric mean          | (ref)                                                                 | 1.04x faster                                                    |

Benchmark hidden because not significant (11): spectral_norm, scimark_sparse_mat_mult, regex_compile, unpickle_list, sympy_sum, generators, bench_mp_pool, sympy_expand, json_dumps, coverage, richards
Ignored benchmarks (4) of results/bm-20230531-3.12.0a4-0fd3163/bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
