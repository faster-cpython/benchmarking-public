
# Results vs. base

- fork: faster-cpython
- ref: nogil_latest
- machine: windows-amd64
- commit hash: 1d39009
- commit date: 2023-04-16
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 193 ms                                                                     | 224 ms: 1.16x slower                                                         |
| chameleon      | 4.39 ms                                                                    | 5.66 ms: 1.29x slower                                                        |
| docutils       | 1.48 sec                                                                   | 1.89 sec: 1.27x slower                                                       |
| html5lib       | 33.7 ms                                                                    | 39.3 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                                      | 1.22x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 145 ms                                                                     | 141 ms: 1.03x faster                                                         |
| float          | 47.2 ms                                                                    | 49.6 ms: 1.05x slower                                                        |
| nbody          | 59.5 ms                                                                    | 89.9 ms: 1.51x slower                                                        |
| Geometric mean | (ref)                                                                      | 1.15x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 120 ms                                                                     | 110 ms: 1.09x faster                                                         |
| regex_effbot   | 1.59 ms                                                                    | 1.53 ms: 1.04x faster                                                        |
| regex_v8       | 13.6 ms                                                                    | 13.2 ms: 1.03x faster                                                        |
| regex_compile  | 78.8 ms                                                                    | 96.4 ms: 1.22x slower                                                        |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 86.5 ms                                                                    | 82.9 ms: 1.04x faster                                                        |
| unpickle             | 8.70 us                                                                    | 9.19 us: 1.06x slower                                                        |
| pickle               | 6.55 us                                                                    | 7.14 us: 1.09x slower                                                        |
| unpickle_list        | 2.59 us                                                                    | 2.86 us: 1.11x slower                                                        |
| json_loads           | 12.4 us                                                                    | 14.6 us: 1.17x slower                                                        |
| xml_etree_generate   | 48.3 ms                                                                    | 57.5 ms: 1.19x slower                                                        |
| pickle_dict          | 18.2 us                                                                    | 21.8 us: 1.19x slower                                                        |
| xml_etree_process    | 33.8 ms                                                                    | 41.7 ms: 1.23x slower                                                        |
| xml_etree_iterparse  | 60.1 ms                                                                    | 74.7 ms: 1.24x slower                                                        |
| json_dumps           | 5.10 ms                                                                    | 6.50 ms: 1.28x slower                                                        |
| pickle_pure_python   | 169 us                                                                     | 218 us: 1.29x slower                                                         |
| unpickle_pure_python | 119 us                                                                     | 159 us: 1.34x slower                                                         |
| Geometric mean       | (ref)                                                                      | 1.16x slower                                                                 |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 15.2 ms                                                                    | 15.4 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                      | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|-----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                                    | 35.3 ms: 1.16x slower                                                        |
| django_template | 20.7 ms                                                                    | 25.5 ms: 1.23x slower                                                        |
| genshi_text     | 13.3 ms                                                                    | 17.7 ms: 1.33x slower                                                        |
| mako            | 6.05 ms                                                                    | 8.95 ms: 1.48x slower                                                        |
| Geometric mean  | (ref)                                                                      | 1.30x slower                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|-------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 742 ms                                                                     | 405 ms: 1.83x faster                                                         |
| async_tree_none         | 295 ms                                                                     | 189 ms: 1.56x faster                                                         |
| async_tree_memoization  | 342 ms                                                                     | 240 ms: 1.42x faster                                                         |
| sqlite_synth            | 1.72 us                                                                    | 1.35 us: 1.27x faster                                                        |
| async_tree_cpu_io_mixed | 465 ms                                                                     | 371 ms: 1.25x faster                                                         |
| regex_dna               | 120 ms                                                                     | 110 ms: 1.09x faster                                                         |
| xml_etree_parse         | 86.5 ms                                                                    | 82.9 ms: 1.04x faster                                                        |
| regex_effbot            | 1.59 ms                                                                    | 1.53 ms: 1.04x faster                                                        |
| pidigits                | 145 ms                                                                     | 141 ms: 1.03x faster                                                         |
| regex_v8                | 13.6 ms                                                                    | 13.2 ms: 1.03x faster                                                        |
| python_startup_no_site  | 15.2 ms                                                                    | 15.4 ms: 1.01x slower                                                        |
| bench_mp_pool           | 61.1 ms                                                                    | 63.9 ms: 1.04x slower                                                        |
| asyncio_tcp             | 466 ms                                                                     | 489 ms: 1.05x slower                                                         |
| float                   | 47.2 ms                                                                    | 49.6 ms: 1.05x slower                                                        |
| unpickle                | 8.70 us                                                                    | 9.19 us: 1.06x slower                                                        |
| mdp                     | 1.51 sec                                                                   | 1.63 sec: 1.08x slower                                                       |
| dulwich_log             | 40.1 ms                                                                    | 43.6 ms: 1.09x slower                                                        |
| gc_traversal            | 1.43 ms                                                                    | 1.56 ms: 1.09x slower                                                        |
| pickle                  | 6.55 us                                                                    | 7.14 us: 1.09x slower                                                        |
| unpickle_list           | 2.59 us                                                                    | 2.86 us: 1.11x slower                                                        |
| json                    | 2.61 ms                                                                    | 2.94 ms: 1.13x slower                                                        |
| create_gc_cycles        | 661 us                                                                     | 748 us: 1.13x slower                                                         |
| generators              | 33.1 ms                                                                    | 37.5 ms: 1.13x slower                                                        |
| pycparser               | 628 ms                                                                     | 713 ms: 1.13x slower                                                         |
| coverage                | 52.5 ms                                                                    | 59.9 ms: 1.14x slower                                                        |
| nqueens                 | 57.3 ms                                                                    | 65.6 ms: 1.15x slower                                                        |
| pyflate                 | 263 ms                                                                     | 302 ms: 1.15x slower                                                         |
| crypto_pyaes            | 45.9 ms                                                                    | 52.7 ms: 1.15x slower                                                        |
| genshi_xml              | 30.5 ms                                                                    | 35.3 ms: 1.16x slower                                                        |
| 2to3                    | 193 ms                                                                     | 224 ms: 1.16x slower                                                         |
| html5lib                | 33.7 ms                                                                    | 39.3 ms: 1.17x slower                                                        |
| thrift                  | 463 us                                                                     | 542 us: 1.17x slower                                                         |
| json_loads              | 12.4 us                                                                    | 14.6 us: 1.17x slower                                                        |
| logging_format          | 6.29 us                                                                    | 7.40 us: 1.18x slower                                                        |
| sympy_str               | 168 ms                                                                     | 198 ms: 1.18x slower                                                         |
| sympy_integrate         | 12.6 ms                                                                    | 14.8 ms: 1.18x slower                                                        |
| sqlglot_normalize       | 168 ms                                                                     | 199 ms: 1.18x slower                                                         |
| logging_simple          | 5.84 us                                                                    | 6.92 us: 1.19x slower                                                        |
| sympy_sum               | 92.0 ms                                                                    | 109 ms: 1.19x slower                                                         |
| xml_etree_generate      | 48.3 ms                                                                    | 57.5 ms: 1.19x slower                                                        |
| sympy_expand            | 269 ms                                                                     | 320 ms: 1.19x slower                                                         |
| pickle_dict             | 18.2 us                                                                    | 21.8 us: 1.19x slower                                                        |
| sqlglot_optimize        | 30.6 ms                                                                    | 36.8 ms: 1.20x slower                                                        |
| coroutines              | 13.9 ms                                                                    | 16.8 ms: 1.21x slower                                                        |
| async_generators        | 169 ms                                                                     | 205 ms: 1.21x slower                                                         |
| regex_compile           | 78.8 ms                                                                    | 96.4 ms: 1.22x slower                                                        |
| telco                   | 3.59 ms                                                                    | 4.41 ms: 1.23x slower                                                        |
| xml_etree_process       | 33.8 ms                                                                    | 41.7 ms: 1.23x slower                                                        |
| django_template         | 20.7 ms                                                                    | 25.5 ms: 1.23x slower                                                        |
| xml_etree_iterparse     | 60.1 ms                                                                    | 74.7 ms: 1.24x slower                                                        |
| spectral_norm           | 62.8 ms                                                                    | 78.8 ms: 1.26x slower                                                        |
| comprehensions          | 15.0 us                                                                    | 19.1 us: 1.27x slower                                                        |
| meteor_contest          | 67.9 ms                                                                    | 86.5 ms: 1.27x slower                                                        |
| docutils                | 1.48 sec                                                                   | 1.89 sec: 1.27x slower                                                       |
| json_dumps              | 5.10 ms                                                                    | 6.50 ms: 1.28x slower                                                        |
| chaos                   | 42.1 ms                                                                    | 53.7 ms: 1.28x slower                                                        |
| go                      | 80.4 ms                                                                    | 103 ms: 1.28x slower                                                         |
| pickle_pure_python      | 169 us                                                                     | 218 us: 1.29x slower                                                         |
| bench_thread_pool       | 798 us                                                                     | 1.03 ms: 1.29x slower                                                        |
| chameleon               | 4.39 ms                                                                    | 5.66 ms: 1.29x slower                                                        |
| sqlglot_transpile       | 1.02 ms                                                                    | 1.33 ms: 1.30x slower                                                        |
| scimark_lu              | 56.0 ms                                                                    | 73.1 ms: 1.30x slower                                                        |
| pprint_safe_repr        | 448 ms                                                                     | 586 ms: 1.31x slower                                                         |
| fannkuch                | 217 ms                                                                     | 285 ms: 1.31x slower                                                         |
| pprint_pformat          | 918 ms                                                                     | 1.21 sec: 1.32x slower                                                       |
| scimark_fft             | 167 ms                                                                     | 220 ms: 1.32x slower                                                         |
| hexiom                  | 3.77 ms                                                                    | 4.97 ms: 1.32x slower                                                        |
| sqlglot_parse           | 848 us                                                                     | 1.12 ms: 1.32x slower                                                        |
| scimark_sparse_mat_mult | 2.25 ms                                                                    | 2.98 ms: 1.33x slower                                                        |
| genshi_text             | 13.3 ms                                                                    | 17.7 ms: 1.33x slower                                                        |
| unpickle_pure_python    | 119 us                                                                     | 159 us: 1.34x slower                                                         |
| richards                | 24.0 ms                                                                    | 32.3 ms: 1.35x slower                                                        |
| scimark_monte_carlo     | 38.0 ms                                                                    | 51.2 ms: 1.35x slower                                                        |
| deepcopy_reduce         | 1.78 us                                                                    | 2.40 us: 1.35x slower                                                        |
| deepcopy                | 199 us                                                                     | 272 us: 1.36x slower                                                         |
| logging_silent          | 54.2 ns                                                                    | 75.0 ns: 1.39x slower                                                        |
| mypy2                   | 209 ms                                                                     | 291 ms: 1.39x slower                                                         |
| deltablue               | 1.94 ms                                                                    | 2.71 ms: 1.40x slower                                                        |
| scimark_sor             | 63.7 ms                                                                    | 89.1 ms: 1.40x slower                                                        |
| raytrace                | 171 ms                                                                     | 241 ms: 1.41x slower                                                         |
| deepcopy_memo           | 20.4 us                                                                    | 29.5 us: 1.45x slower                                                        |
| mako                    | 6.05 ms                                                                    | 8.95 ms: 1.48x slower                                                        |
| nbody                   | 59.5 ms                                                                    | 89.9 ms: 1.51x slower                                                        |
| unpack_sequence         | 26.2 ns                                                                    | 55.2 ns: 2.11x slower                                                        |
| Geometric mean          | (ref)                                                                      | 1.17x slower                                                                 |

Benchmark hidden because not significant (3): pickle_list, pathlib, python_startup
Ignored benchmarks (1) of results/bm-20230110-3.12.0a4-3d5d3f7/bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7.json: dask


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.16x
- 99% likely to have a slowdown of 1.14x
