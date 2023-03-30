
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b2
- machine: windows-amd64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.05x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 211 ms: 1.04x slower                                            |
| chameleon      | 5.15 ms                                                                  | 5.59 ms: 1.08x slower                                           |
| docutils       | 1.59 sec                                                                 | 1.66 sec: 1.04x slower                                          |
| html5lib       | 38.5 ms                                                                  | 41.4 ms: 1.08x slower                                           |
| tornado_http   | 91.8 ms                                                                  | 95.3 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                                    | 1.05x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 70.1 ms: 1.01x faster                                           |
| float          | 53.3 ms                                                                  | 54.5 ms: 1.02x slower                                           |
| pidigits       | 147 ms                                                                   | 153 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                                    | 1.02x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.63 ms                                                                  | 1.39 ms: 1.18x faster                                           |
| regex_dna      | 115 ms                                                                   | 120 ms: 1.04x slower                                            |
| regex_v8       | 13.5 ms                                                                  | 14.4 ms: 1.07x slower                                           |
| regex_compile  | 89.7 ms                                                                  | 97.0 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_dict          | 18.6 us                                                                  | 17.4 us: 1.07x faster                                           |
| pickle_list          | 2.70 us                                                                  | 2.64 us: 1.02x faster                                           |
| unpickle_list        | 2.80 us                                                                  | 2.76 us: 1.01x faster                                           |
| unpickle             | 8.01 us                                                                  | 8.07 us: 1.01x slower                                           |
| xml_etree_generate   | 52.3 ms                                                                  | 54.1 ms: 1.04x slower                                           |
| json_loads           | 13.5 us                                                                  | 14.1 us: 1.04x slower                                           |
| pickle               | 6.47 us                                                                  | 6.74 us: 1.04x slower                                           |
| xml_etree_parse      | 92.1 ms                                                                  | 96.7 ms: 1.05x slower                                           |
| pickle_pure_python   | 203 us                                                                   | 216 us: 1.06x slower                                            |
| json_dumps           | 7.71 ms                                                                  | 8.21 ms: 1.06x slower                                           |
| xml_etree_process    | 36.6 ms                                                                  | 39.1 ms: 1.07x slower                                           |
| unpickle_pure_python | 150 us                                                                   | 164 us: 1.10x slower                                            |
| Geometric mean       | (ref)                                                                    | 1.03x slower                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 15.4 ms                                                                  | 15.8 ms: 1.03x slower                                           |
| python_startup         | 18.4 ms                                                                  | 19.0 ms: 1.04x slower                                           |
| Geometric mean         | (ref)                                                                    | 1.03x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text     | 17.3 ms                                                                  | 17.9 ms: 1.04x slower                                           |
| django_template | 23.9 ms                                                                  | 25.1 ms: 1.05x slower                                           |
| mako            | 7.20 ms                                                                  | 7.62 ms: 1.06x slower                                           |
| genshi_xml      | 38.0 ms                                                                  | 40.2 ms: 1.06x slower                                           |
| Geometric mean  | (ref)                                                                    | 1.05x slower                                                    |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot            | 1.63 ms                                                                  | 1.39 ms: 1.18x faster                                           |
| logging_format          | 7.13 us                                                                  | 6.39 us: 1.11x faster                                           |
| logging_simple          | 6.60 us                                                                  | 5.94 us: 1.11x faster                                           |
| pickle_dict             | 18.6 us                                                                  | 17.4 us: 1.07x faster                                           |
| pickle_list             | 2.70 us                                                                  | 2.64 us: 1.02x faster                                           |
| spectral_norm           | 71.8 ms                                                                  | 70.6 ms: 1.02x faster                                           |
| richards                | 32.1 ms                                                                  | 31.6 ms: 1.02x faster                                           |
| unpickle_list           | 2.80 us                                                                  | 2.76 us: 1.01x faster                                           |
| nbody                   | 70.9 ms                                                                  | 70.1 ms: 1.01x faster                                           |
| unpickle                | 8.01 us                                                                  | 8.07 us: 1.01x slower                                           |
| create_gc_cycles        | 666 us                                                                   | 675 us: 1.01x slower                                            |
| deltablue               | 2.68 ms                                                                  | 2.72 ms: 1.02x slower                                           |
| logging_silent          | 71.0 ns                                                                  | 72.2 ns: 1.02x slower                                           |
| sqlite_synth            | 1.67 us                                                                  | 1.71 us: 1.02x slower                                           |
| float                   | 53.3 ms                                                                  | 54.5 ms: 1.02x slower                                           |
| pathlib                 | 72.9 ms                                                                  | 74.8 ms: 1.03x slower                                           |
| scimark_lu              | 62.8 ms                                                                  | 64.6 ms: 1.03x slower                                           |
| go                      | 97.5 ms                                                                  | 100 ms: 1.03x slower                                            |
| unpack_sequence         | 43.1 ns                                                                  | 44.3 ns: 1.03x slower                                           |
| python_startup_no_site  | 15.4 ms                                                                  | 15.8 ms: 1.03x slower                                           |
| scimark_sor             | 77.7 ms                                                                  | 80.0 ms: 1.03x slower                                           |
| deepcopy_memo           | 25.3 us                                                                  | 26.1 us: 1.03x slower                                           |
| telco                   | 3.93 ms                                                                  | 4.05 ms: 1.03x slower                                           |
| sympy_str               | 184 ms                                                                   | 190 ms: 1.03x slower                                            |
| bench_mp_pool           | 61.2 ms                                                                  | 63.3 ms: 1.03x slower                                           |
| python_startup          | 18.4 ms                                                                  | 19.0 ms: 1.04x slower                                           |
| xml_etree_generate      | 52.3 ms                                                                  | 54.1 ms: 1.04x slower                                           |
| 2to3                    | 204 ms                                                                   | 211 ms: 1.04x slower                                            |
| genshi_text             | 17.3 ms                                                                  | 17.9 ms: 1.04x slower                                           |
| raytrace                | 206 ms                                                                   | 213 ms: 1.04x slower                                            |
| gc_traversal            | 1.40 ms                                                                  | 1.46 ms: 1.04x slower                                           |
| pylint                  | 319 ms                                                                   | 331 ms: 1.04x slower                                            |
| tornado_http            | 91.8 ms                                                                  | 95.3 ms: 1.04x slower                                           |
| async_generators        | 180 ms                                                                   | 187 ms: 1.04x slower                                            |
| sympy_sum               | 98.9 ms                                                                  | 103 ms: 1.04x slower                                            |
| regex_dna               | 115 ms                                                                   | 120 ms: 1.04x slower                                            |
| docutils                | 1.59 sec                                                                 | 1.66 sec: 1.04x slower                                          |
| bench_thread_pool       | 856 us                                                                   | 889 us: 1.04x slower                                            |
| pyflate                 | 302 ms                                                                   | 314 ms: 1.04x slower                                            |
| json_loads              | 13.5 us                                                                  | 14.1 us: 1.04x slower                                           |
| sympy_integrate         | 13.7 ms                                                                  | 14.2 ms: 1.04x slower                                           |
| fannkuch                | 255 ms                                                                   | 266 ms: 1.04x slower                                            |
| pickle                  | 6.47 us                                                                  | 6.74 us: 1.04x slower                                           |
| pidigits                | 147 ms                                                                   | 153 ms: 1.04x slower                                            |
| scimark_fft             | 183 ms                                                                   | 191 ms: 1.04x slower                                            |
| sympy_expand            | 298 ms                                                                   | 312 ms: 1.05x slower                                            |
| mdp                     | 1.67 sec                                                                 | 1.75 sec: 1.05x slower                                          |
| xml_etree_parse         | 92.1 ms                                                                  | 96.7 ms: 1.05x slower                                           |
| django_template         | 23.9 ms                                                                  | 25.1 ms: 1.05x slower                                           |
| dask                    | 267 ms                                                                   | 280 ms: 1.05x slower                                            |
| coroutines              | 14.8 ms                                                                  | 15.6 ms: 1.05x slower                                           |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.77 ms: 1.05x slower                                           |
| mako                    | 7.20 ms                                                                  | 7.62 ms: 1.06x slower                                           |
| genshi_xml              | 38.0 ms                                                                  | 40.2 ms: 1.06x slower                                           |
| nqueens                 | 65.1 ms                                                                  | 68.9 ms: 1.06x slower                                           |
| meteor_contest          | 74.4 ms                                                                  | 78.7 ms: 1.06x slower                                           |
| pprint_pformat          | 1.05 sec                                                                 | 1.11 sec: 1.06x slower                                          |
| thrift                  | 487 us                                                                   | 516 us: 1.06x slower                                            |
| dulwich_log             | 43.4 ms                                                                  | 46.1 ms: 1.06x slower                                           |
| pickle_pure_python      | 203 us                                                                   | 216 us: 1.06x slower                                            |
| generators              | 33.5 ms                                                                  | 35.7 ms: 1.06x slower                                           |
| json_dumps              | 7.71 ms                                                                  | 8.21 ms: 1.06x slower                                           |
| aiohttp                 | 864 us                                                                   | 921 us: 1.07x slower                                            |
| deepcopy_reduce         | 2.06 us                                                                  | 2.19 us: 1.07x slower                                           |
| async_tree_io           | 744 ms                                                                   | 794 ms: 1.07x slower                                            |
| xml_etree_process       | 36.6 ms                                                                  | 39.1 ms: 1.07x slower                                           |
| async_tree_memoization  | 374 ms                                                                   | 400 ms: 1.07x slower                                            |
| pprint_safe_repr        | 512 ms                                                                   | 548 ms: 1.07x slower                                            |
| regex_v8                | 13.5 ms                                                                  | 14.4 ms: 1.07x slower                                           |
| sqlglot_normalize       | 189 ms                                                                   | 203 ms: 1.07x slower                                            |
| crypto_pyaes            | 48.3 ms                                                                  | 51.8 ms: 1.07x slower                                           |
| async_tree_none         | 313 ms                                                                   | 336 ms: 1.07x slower                                            |
| html5lib                | 38.5 ms                                                                  | 41.4 ms: 1.08x slower                                           |
| regex_compile           | 89.7 ms                                                                  | 97.0 ms: 1.08x slower                                           |
| chameleon               | 5.15 ms                                                                  | 5.59 ms: 1.08x slower                                           |
| hexiom                  | 4.46 ms                                                                  | 4.84 ms: 1.08x slower                                           |
| sqlglot_optimize        | 34.5 ms                                                                  | 37.5 ms: 1.09x slower                                           |
| deepcopy                | 240 us                                                                   | 261 us: 1.09x slower                                            |
| pycparser               | 686 ms                                                                   | 750 ms: 1.09x slower                                            |
| chaos                   | 47.3 ms                                                                  | 51.8 ms: 1.10x slower                                           |
| unpickle_pure_python    | 150 us                                                                   | 164 us: 1.10x slower                                            |
| asyncio_tcp             | 674 ms                                                                   | 742 ms: 1.10x slower                                            |
| comprehensions          | 15.4 us                                                                  | 18.2 us: 1.18x slower                                           |
| sqlglot_transpile       | 1.13 ms                                                                  | 1.42 ms: 1.25x slower                                           |
| sqlglot_parse           | 929 us                                                                   | 1.21 ms: 1.30x slower                                           |
| coverage                | 55.3 ms                                                                  | 106 ms: 1.91x slower                                            |
| Geometric mean          | (ref)                                                                    | 1.05x slower                                                    |

Benchmark hidden because not significant (7): sqlalchemy_imperative, sqlalchemy_declarative, xml_etree_iterparse, scimark_monte_carlo, json, async_tree_cpu_io_mixed, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging
