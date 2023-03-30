
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b3
- machine: windows-amd64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.05x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 212 ms: 1.04x slower                                            |
| chameleon      | 5.15 ms                                                                  | 5.63 ms: 1.09x slower                                           |
| docutils       | 1.59 sec                                                                 | 1.66 sec: 1.04x slower                                          |
| html5lib       | 38.5 ms                                                                  | 41.2 ms: 1.07x slower                                           |
| tornado_http   | 91.8 ms                                                                  | 94.8 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                                    | 1.06x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 71.9 ms: 1.01x slower                                           |
| pidigits       | 147 ms                                                                   | 154 ms: 1.05x slower                                            |
| float          | 53.3 ms                                                                  | 57.2 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                                    | 1.04x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.63 ms                                                                  | 1.62 ms: 1.01x faster                                           |
| regex_compile  | 89.7 ms                                                                  | 94.2 ms: 1.05x slower                                           |
| regex_dna      | 115 ms                                                                   | 127 ms: 1.10x slower                                            |
| regex_v8       | 13.5 ms                                                                  | 15.2 ms: 1.13x slower                                           |
| Geometric mean | (ref)                                                                    | 1.07x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_dict          | 18.6 us                                                                  | 17.7 us: 1.05x faster                                           |
| unpickle_list        | 2.80 us                                                                  | 2.71 us: 1.03x faster                                           |
| xml_etree_iterparse  | 61.8 ms                                                                  | 63.3 ms: 1.02x slower                                           |
| json_dumps           | 7.71 ms                                                                  | 7.98 ms: 1.03x slower                                           |
| unpickle             | 8.01 us                                                                  | 8.33 us: 1.04x slower                                           |
| pickle_list          | 2.70 us                                                                  | 2.81 us: 1.04x slower                                           |
| pickle_pure_python   | 203 us                                                                   | 212 us: 1.04x slower                                            |
| json_loads           | 13.5 us                                                                  | 14.2 us: 1.05x slower                                           |
| unpickle_pure_python | 150 us                                                                   | 158 us: 1.06x slower                                            |
| pickle               | 6.47 us                                                                  | 6.83 us: 1.06x slower                                           |
| xml_etree_parse      | 92.1 ms                                                                  | 97.4 ms: 1.06x slower                                           |
| xml_etree_process    | 36.6 ms                                                                  | 38.9 ms: 1.06x slower                                           |
| xml_etree_generate   | 52.3 ms                                                                  | 55.8 ms: 1.07x slower                                           |
| Geometric mean       | (ref)                                                                    | 1.03x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 18.4 ms                                                                  | 19.4 ms: 1.05x slower                                           |
| python_startup_no_site | 15.4 ms                                                                  | 16.4 ms: 1.07x slower                                           |
| Geometric mean         | (ref)                                                                    | 1.06x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.20 ms                                                                  | 7.38 ms: 1.02x slower                                           |
| django_template | 23.9 ms                                                                  | 25.4 ms: 1.06x slower                                           |
| genshi_text     | 17.3 ms                                                                  | 18.6 ms: 1.08x slower                                           |
| genshi_xml      | 38.0 ms                                                                  | 41.0 ms: 1.08x slower                                           |
| Geometric mean  | (ref)                                                                    | 1.06x slower                                                    |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| unpack_sequence         | 43.1 ns                                                                  | 36.8 ns: 1.17x faster                                           |
| logging_simple          | 6.60 us                                                                  | 5.96 us: 1.11x faster                                           |
| logging_format          | 7.13 us                                                                  | 6.43 us: 1.11x faster                                           |
| pickle_dict             | 18.6 us                                                                  | 17.7 us: 1.05x faster                                           |
| richards                | 32.1 ms                                                                  | 30.7 ms: 1.05x faster                                           |
| unpickle_list           | 2.80 us                                                                  | 2.71 us: 1.03x faster                                           |
| sqlalchemy_imperative   | 10.4 ms                                                                  | 10.3 ms: 1.01x faster                                           |
| regex_effbot            | 1.63 ms                                                                  | 1.62 ms: 1.01x faster                                           |
| mdp                     | 1.67 sec                                                                 | 1.66 sec: 1.01x faster                                          |
| scimark_monte_carlo     | 45.8 ms                                                                  | 45.4 ms: 1.01x faster                                           |
| flaskblogging           | 2.04 sec                                                                 | 2.05 sec: 1.01x slower                                          |
| pathlib                 | 72.9 ms                                                                  | 73.6 ms: 1.01x slower                                           |
| scimark_lu              | 62.8 ms                                                                  | 63.6 ms: 1.01x slower                                           |
| nbody                   | 70.9 ms                                                                  | 71.9 ms: 1.01x slower                                           |
| sympy_sum               | 98.9 ms                                                                  | 100 ms: 1.02x slower                                            |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.68 ms: 1.02x slower                                           |
| xml_etree_iterparse     | 61.8 ms                                                                  | 63.3 ms: 1.02x slower                                           |
| logging_silent          | 71.0 ns                                                                  | 72.7 ns: 1.02x slower                                           |
| mako                    | 7.20 ms                                                                  | 7.38 ms: 1.02x slower                                           |
| sympy_expand            | 298 ms                                                                   | 306 ms: 1.02x slower                                            |
| deepcopy_memo           | 25.3 us                                                                  | 26.0 us: 1.03x slower                                           |
| create_gc_cycles        | 666 us                                                                   | 686 us: 1.03x slower                                            |
| sympy_str               | 184 ms                                                                   | 190 ms: 1.03x slower                                            |
| scimark_fft             | 183 ms                                                                   | 188 ms: 1.03x slower                                            |
| tornado_http            | 91.8 ms                                                                  | 94.8 ms: 1.03x slower                                           |
| json_dumps              | 7.71 ms                                                                  | 7.98 ms: 1.03x slower                                           |
| sqlalchemy_declarative  | 83.1 ms                                                                  | 86.0 ms: 1.04x slower                                           |
| meteor_contest          | 74.4 ms                                                                  | 77.1 ms: 1.04x slower                                           |
| pylint                  | 319 ms                                                                   | 331 ms: 1.04x slower                                            |
| deltablue               | 2.68 ms                                                                  | 2.78 ms: 1.04x slower                                           |
| aiohttp                 | 864 us                                                                   | 897 us: 1.04x slower                                            |
| unpickle                | 8.01 us                                                                  | 8.33 us: 1.04x slower                                           |
| 2to3                    | 204 ms                                                                   | 212 ms: 1.04x slower                                            |
| sqlglot_optimize        | 34.5 ms                                                                  | 35.9 ms: 1.04x slower                                           |
| bench_thread_pool       | 856 us                                                                   | 890 us: 1.04x slower                                            |
| pickle_list             | 2.70 us                                                                  | 2.81 us: 1.04x slower                                           |
| sqlite_synth            | 1.67 us                                                                  | 1.74 us: 1.04x slower                                           |
| sympy_integrate         | 13.7 ms                                                                  | 14.2 ms: 1.04x slower                                           |
| docutils                | 1.59 sec                                                                 | 1.66 sec: 1.04x slower                                          |
| pickle_pure_python      | 203 us                                                                   | 212 us: 1.04x slower                                            |
| raytrace                | 206 ms                                                                   | 215 ms: 1.04x slower                                            |
| json_loads              | 13.5 us                                                                  | 14.2 us: 1.05x slower                                           |
| dulwich_log             | 43.4 ms                                                                  | 45.5 ms: 1.05x slower                                           |
| pidigits                | 147 ms                                                                   | 154 ms: 1.05x slower                                            |
| sqlglot_normalize       | 189 ms                                                                   | 198 ms: 1.05x slower                                            |
| regex_compile           | 89.7 ms                                                                  | 94.2 ms: 1.05x slower                                           |
| async_tree_io           | 744 ms                                                                   | 781 ms: 1.05x slower                                            |
| telco                   | 3.93 ms                                                                  | 4.13 ms: 1.05x slower                                           |
| dask                    | 267 ms                                                                   | 281 ms: 1.05x slower                                            |
| pyflate                 | 302 ms                                                                   | 318 ms: 1.05x slower                                            |
| python_startup          | 18.4 ms                                                                  | 19.4 ms: 1.05x slower                                           |
| crypto_pyaes            | 48.3 ms                                                                  | 50.9 ms: 1.05x slower                                           |
| unpickle_pure_python    | 150 us                                                                   | 158 us: 1.06x slower                                            |
| generators              | 33.5 ms                                                                  | 35.4 ms: 1.06x slower                                           |
| pickle                  | 6.47 us                                                                  | 6.83 us: 1.06x slower                                           |
| thrift                  | 487 us                                                                   | 514 us: 1.06x slower                                            |
| xml_etree_parse         | 92.1 ms                                                                  | 97.4 ms: 1.06x slower                                           |
| coroutines              | 14.8 ms                                                                  | 15.7 ms: 1.06x slower                                           |
| pprint_safe_repr        | 512 ms                                                                   | 541 ms: 1.06x slower                                            |
| gc_traversal            | 1.40 ms                                                                  | 1.49 ms: 1.06x slower                                           |
| xml_etree_process       | 36.6 ms                                                                  | 38.9 ms: 1.06x slower                                           |
| async_generators        | 180 ms                                                                   | 192 ms: 1.06x slower                                            |
| django_template         | 23.9 ms                                                                  | 25.4 ms: 1.06x slower                                           |
| python_startup_no_site  | 15.4 ms                                                                  | 16.4 ms: 1.07x slower                                           |
| xml_etree_generate      | 52.3 ms                                                                  | 55.8 ms: 1.07x slower                                           |
| go                      | 97.5 ms                                                                  | 104 ms: 1.07x slower                                            |
| html5lib                | 38.5 ms                                                                  | 41.2 ms: 1.07x slower                                           |
| pprint_pformat          | 1.05 sec                                                                 | 1.12 sec: 1.07x slower                                          |
| pycparser               | 686 ms                                                                   | 735 ms: 1.07x slower                                            |
| float                   | 53.3 ms                                                                  | 57.2 ms: 1.07x slower                                           |
| async_tree_memoization  | 374 ms                                                                   | 402 ms: 1.08x slower                                            |
| genshi_text             | 17.3 ms                                                                  | 18.6 ms: 1.08x slower                                           |
| genshi_xml              | 38.0 ms                                                                  | 41.0 ms: 1.08x slower                                           |
| deepcopy_reduce         | 2.06 us                                                                  | 2.22 us: 1.08x slower                                           |
| hexiom                  | 4.46 ms                                                                  | 4.82 ms: 1.08x slower                                           |
| async_tree_none         | 313 ms                                                                   | 339 ms: 1.08x slower                                            |
| fannkuch                | 255 ms                                                                   | 278 ms: 1.09x slower                                            |
| nqueens                 | 65.1 ms                                                                  | 71.0 ms: 1.09x slower                                           |
| chameleon               | 5.15 ms                                                                  | 5.63 ms: 1.09x slower                                           |
| chaos                   | 47.3 ms                                                                  | 51.8 ms: 1.09x slower                                           |
| bench_mp_pool           | 61.2 ms                                                                  | 67.0 ms: 1.10x slower                                           |
| regex_dna               | 115 ms                                                                   | 127 ms: 1.10x slower                                            |
| deepcopy                | 240 us                                                                   | 265 us: 1.11x slower                                            |
| regex_v8                | 13.5 ms                                                                  | 15.2 ms: 1.13x slower                                           |
| asyncio_tcp             | 674 ms                                                                   | 762 ms: 1.13x slower                                            |
| comprehensions          | 15.4 us                                                                  | 18.7 us: 1.22x slower                                           |
| sqlglot_transpile       | 1.13 ms                                                                  | 1.41 ms: 1.25x slower                                           |
| sqlglot_parse           | 929 us                                                                   | 1.21 ms: 1.30x slower                                           |
| coverage                | 55.3 ms                                                                  | 108 ms: 1.95x slower                                            |
| Geometric mean          | (ref)                                                                    | 1.05x slower                                                    |

Benchmark hidden because not significant (5): spectral_norm, scimark_sor, async_tree_cpu_io_mixed, json, mypy2
