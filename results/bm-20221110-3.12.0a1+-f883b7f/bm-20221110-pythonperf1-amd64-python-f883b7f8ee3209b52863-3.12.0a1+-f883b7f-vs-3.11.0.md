
# Results vs. 3.11.0

- fork: python
- ref: f883b7f8ee3209b52863
- machine: windows-amd64
- commit hash: f883b7f
- commit date: 2022-11-10
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 200 ms: 1.02x faster                                                        |
| chameleon      | 5.15 ms                                                                  | 4.97 ms: 1.04x faster                                                       |
| html5lib       | 38.5 ms                                                                  | 36.2 ms: 1.06x faster                                                       |
| tornado_http   | 91.8 ms                                                                  | 93.2 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 62.7 ms: 1.13x faster                                                       |
| float          | 53.3 ms                                                                  | 52.3 ms: 1.02x faster                                                       |
| pidigits       | 147 ms                                                                   | 150 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 89.7 ms                                                                  | 87.2 ms: 1.03x faster                                                       |
| regex_effbot   | 1.63 ms                                                                  | 1.60 ms: 1.02x faster                                                       |
| regex_v8       | 13.5 ms                                                                  | 14.0 ms: 1.04x slower                                                       |
| regex_dna      | 115 ms                                                                   | 122 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.48 ms: 1.41x faster                                                       |
| unpickle_list        | 2.80 us                                                                  | 2.60 us: 1.08x faster                                                       |
| pickle_pure_python   | 203 us                                                                   | 190 us: 1.07x faster                                                        |
| json_loads           | 13.5 us                                                                  | 13.1 us: 1.03x faster                                                       |
| xml_etree_parse      | 92.1 ms                                                                  | 90.9 ms: 1.01x faster                                                       |
| unpickle_pure_python | 150 us                                                                   | 148 us: 1.01x faster                                                        |
| pickle_dict          | 18.6 us                                                                  | 19.1 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 61.8 ms                                                                  | 63.9 ms: 1.03x slower                                                       |
| pickle_list          | 2.70 us                                                                  | 2.82 us: 1.04x slower                                                       |
| pickle               | 6.47 us                                                                  | 7.14 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                                    | 1.03x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 18.4 ms                                                                  | 18.9 ms: 1.03x slower                                                       |
| python_startup_no_site | 15.4 ms                                                                  | 15.8 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                                    | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.20 ms                                                                  | 6.58 ms: 1.09x faster                                                       |
| django_template | 23.9 ms                                                                  | 22.1 ms: 1.08x faster                                                       |
| genshi_text     | 17.3 ms                                                                  | 16.3 ms: 1.06x faster                                                       |
| genshi_xml      | 38.0 ms                                                                  | 35.9 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                                    | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 7.71 ms                                                                  | 5.48 ms: 1.41x faster                                                       |
| unpack_sequence         | 43.1 ns                                                                  | 32.4 ns: 1.33x faster                                                       |
| mypy2                   | 276 ms                                                                   | 225 ms: 1.23x faster                                                        |
| richards                | 32.1 ms                                                                  | 26.8 ms: 1.20x faster                                                       |
| json                    | 3.20 ms                                                                  | 2.70 ms: 1.18x faster                                                       |
| deltablue               | 2.68 ms                                                                  | 2.37 ms: 1.13x faster                                                       |
| nbody                   | 70.9 ms                                                                  | 62.7 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.36 ms: 1.12x faster                                                       |
| logging_silent          | 71.0 ns                                                                  | 64.1 ns: 1.11x faster                                                       |
| scimark_monte_carlo     | 45.8 ms                                                                  | 41.3 ms: 1.11x faster                                                       |
| mako                    | 7.20 ms                                                                  | 6.58 ms: 1.09x faster                                                       |
| go                      | 97.5 ms                                                                  | 89.7 ms: 1.09x faster                                                       |
| raytrace                | 206 ms                                                                   | 190 ms: 1.08x faster                                                        |
| unpickle_list           | 2.80 us                                                                  | 2.60 us: 1.08x faster                                                       |
| django_template         | 23.9 ms                                                                  | 22.1 ms: 1.08x faster                                                       |
| pickle_pure_python      | 203 us                                                                   | 190 us: 1.07x faster                                                        |
| crypto_pyaes            | 48.3 ms                                                                  | 45.3 ms: 1.07x faster                                                       |
| mdp                     | 1.67 sec                                                                 | 1.57 sec: 1.06x faster                                                      |
| scimark_fft             | 183 ms                                                                   | 172 ms: 1.06x faster                                                        |
| spectral_norm           | 71.8 ms                                                                  | 67.5 ms: 1.06x faster                                                       |
| html5lib                | 38.5 ms                                                                  | 36.2 ms: 1.06x faster                                                       |
| genshi_text             | 17.3 ms                                                                  | 16.3 ms: 1.06x faster                                                       |
| genshi_xml              | 38.0 ms                                                                  | 35.9 ms: 1.06x faster                                                       |
| sqlglot_optimize        | 34.5 ms                                                                  | 32.6 ms: 1.06x faster                                                       |
| pprint_safe_repr        | 512 ms                                                                   | 485 ms: 1.06x faster                                                        |
| meteor_contest          | 74.4 ms                                                                  | 70.5 ms: 1.05x faster                                                       |
| scimark_sor             | 77.7 ms                                                                  | 73.7 ms: 1.05x faster                                                       |
| nqueens                 | 65.1 ms                                                                  | 61.8 ms: 1.05x faster                                                       |
| sympy_expand            | 298 ms                                                                   | 285 ms: 1.05x faster                                                        |
| pyflate                 | 302 ms                                                                   | 290 ms: 1.04x faster                                                        |
| chaos                   | 47.3 ms                                                                  | 45.4 ms: 1.04x faster                                                       |
| sqlglot_transpile       | 1.13 ms                                                                  | 1.09 ms: 1.04x faster                                                       |
| pprint_pformat          | 1.05 sec                                                                 | 1.01 sec: 1.04x faster                                                      |
| chameleon               | 5.15 ms                                                                  | 4.97 ms: 1.04x faster                                                       |
| fannkuch                | 255 ms                                                                   | 247 ms: 1.03x faster                                                        |
| json_loads              | 13.5 us                                                                  | 13.1 us: 1.03x faster                                                       |
| regex_compile           | 89.7 ms                                                                  | 87.2 ms: 1.03x faster                                                       |
| sympy_integrate         | 13.7 ms                                                                  | 13.3 ms: 1.03x faster                                                       |
| sqlglot_normalize       | 189 ms                                                                   | 184 ms: 1.03x faster                                                        |
| hexiom                  | 4.46 ms                                                                  | 4.34 ms: 1.03x faster                                                       |
| deepcopy_memo           | 25.3 us                                                                  | 24.7 us: 1.03x faster                                                       |
| pycparser               | 686 ms                                                                   | 669 ms: 1.03x faster                                                        |
| regex_effbot            | 1.63 ms                                                                  | 1.60 ms: 1.02x faster                                                       |
| 2to3                    | 204 ms                                                                   | 200 ms: 1.02x faster                                                        |
| coverage                | 55.3 ms                                                                  | 54.2 ms: 1.02x faster                                                       |
| coroutines              | 14.8 ms                                                                  | 14.5 ms: 1.02x faster                                                       |
| float                   | 53.3 ms                                                                  | 52.3 ms: 1.02x faster                                                       |
| async_generators        | 180 ms                                                                   | 177 ms: 1.02x faster                                                        |
| telco                   | 3.93 ms                                                                  | 3.86 ms: 1.02x faster                                                       |
| thrift                  | 487 us                                                                   | 479 us: 1.01x faster                                                        |
| bench_thread_pool       | 856 us                                                                   | 843 us: 1.01x faster                                                        |
| sympy_sum               | 98.9 ms                                                                  | 97.5 ms: 1.01x faster                                                       |
| xml_etree_parse         | 92.1 ms                                                                  | 90.9 ms: 1.01x faster                                                       |
| deepcopy_reduce         | 2.06 us                                                                  | 2.03 us: 1.01x faster                                                       |
| logging_format          | 7.13 us                                                                  | 7.05 us: 1.01x faster                                                       |
| unpickle_pure_python    | 150 us                                                                   | 148 us: 1.01x faster                                                        |
| scimark_lu              | 62.8 ms                                                                  | 62.4 ms: 1.01x faster                                                       |
| sympy_str               | 184 ms                                                                   | 183 ms: 1.01x faster                                                        |
| dulwich_log             | 43.4 ms                                                                  | 43.8 ms: 1.01x slower                                                       |
| tornado_http            | 91.8 ms                                                                  | 93.2 ms: 1.01x slower                                                       |
| pickle_dict             | 18.6 us                                                                  | 19.1 us: 1.02x slower                                                       |
| pidigits                | 147 ms                                                                   | 150 ms: 1.02x slower                                                        |
| python_startup          | 18.4 ms                                                                  | 18.9 ms: 1.03x slower                                                       |
| python_startup_no_site  | 15.4 ms                                                                  | 15.8 ms: 1.03x slower                                                       |
| create_gc_cycles        | 666 us                                                                   | 688 us: 1.03x slower                                                        |
| bench_mp_pool           | 61.2 ms                                                                  | 63.2 ms: 1.03x slower                                                       |
| xml_etree_iterparse     | 61.8 ms                                                                  | 63.9 ms: 1.03x slower                                                       |
| comprehensions          | 15.4 us                                                                  | 15.9 us: 1.04x slower                                                       |
| regex_v8                | 13.5 ms                                                                  | 14.0 ms: 1.04x slower                                                       |
| async_tree_memoization  | 374 ms                                                                   | 389 ms: 1.04x slower                                                        |
| pickle_list             | 2.70 us                                                                  | 2.82 us: 1.04x slower                                                       |
| async_tree_io           | 744 ms                                                                   | 782 ms: 1.05x slower                                                        |
| async_tree_none         | 313 ms                                                                   | 330 ms: 1.05x slower                                                        |
| gc_traversal            | 1.40 ms                                                                  | 1.48 ms: 1.05x slower                                                       |
| regex_dna               | 115 ms                                                                   | 122 ms: 1.06x slower                                                        |
| asyncio_tcp             | 674 ms                                                                   | 714 ms: 1.06x slower                                                        |
| sqlite_synth            | 1.67 us                                                                  | 1.79 us: 1.07x slower                                                       |
| pickle                  | 6.47 us                                                                  | 7.14 us: 1.10x slower                                                       |
| Geometric mean          | (ref)                                                                    | 1.03x faster                                                                |

Benchmark hidden because not significant (11): sqlglot_parse, async_tree_cpu_io_mixed, docutils, xml_etree_generate, logging_simple, xml_etree_process, generators, unpickle, dask, deepcopy, pathlib
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
