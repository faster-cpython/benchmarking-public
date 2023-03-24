
# Results vs. 3.11.0

- fork: python
- ref: d49409196e0c73c38e3f
- machine: windows-amd64
- commit hash: d494091
- commit date: 2023-03-24
- overall geometric mean: 1.11x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 194 ms: 1.05x faster                                                        |
| chameleon      | 5.15 ms                                                                  | 4.30 ms: 1.20x faster                                                       |
| docutils       | 1.59 sec                                                                 | 1.51 sec: 1.06x faster                                                      |
| html5lib       | 38.5 ms                                                                  | 35.5 ms: 1.08x faster                                                       |
| tornado_http   | 91.8 ms                                                                  | 86.7 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 55.6 ms: 1.27x faster                                                       |
| float          | 53.3 ms                                                                  | 46.0 ms: 1.16x faster                                                       |
| pidigits       | 147 ms                                                                   | 146 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                    | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 89.7 ms                                                                  | 79.6 ms: 1.13x faster                                                       |
| regex_v8       | 13.5 ms                                                                  | 13.8 ms: 1.03x slower                                                       |
| regex_dna      | 115 ms                                                                   | 122 ms: 1.06x slower                                                        |
| regex_effbot   | 1.63 ms                                                                  | 1.83 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.44 ms: 1.42x faster                                                       |
| unpickle_pure_python | 150 us                                                                   | 117 us: 1.28x faster                                                        |
| pickle_pure_python   | 203 us                                                                   | 168 us: 1.21x faster                                                        |
| xml_etree_process    | 36.6 ms                                                                  | 33.9 ms: 1.08x faster                                                       |
| xml_etree_parse      | 92.1 ms                                                                  | 87.3 ms: 1.06x faster                                                       |
| xml_etree_generate   | 52.3 ms                                                                  | 50.0 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 61.8 ms                                                                  | 59.2 ms: 1.04x faster                                                       |
| unpickle_list        | 2.80 us                                                                  | 2.70 us: 1.04x faster                                                       |
| json_loads           | 13.5 us                                                                  | 13.4 us: 1.01x faster                                                       |
| unpickle             | 8.01 us                                                                  | 7.96 us: 1.01x faster                                                       |
| pickle_list          | 2.70 us                                                                  | 2.78 us: 1.03x slower                                                       |
| pickle               | 6.47 us                                                                  | 6.65 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                                    | 1.08x faster                                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 18.4 ms                                                                  | 18.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.3 ms                                                                  | 13.8 ms: 1.25x faster                                                       |
| genshi_xml      | 38.0 ms                                                                  | 30.5 ms: 1.25x faster                                                       |
| django_template | 23.9 ms                                                                  | 19.9 ms: 1.20x faster                                                       |
| mako            | 7.20 ms                                                                  | 6.10 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                                    | 1.22x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 33.5 ms                                                                  | 20.9 ms: 1.61x faster                                                       |
| unpack_sequence         | 43.1 ns                                                                  | 27.4 ns: 1.57x faster                                                       |
| asyncio_tcp             | 674 ms                                                                   | 469 ms: 1.44x faster                                                        |
| json_dumps              | 7.71 ms                                                                  | 5.44 ms: 1.42x faster                                                       |
| deltablue               | 2.68 ms                                                                  | 1.91 ms: 1.40x faster                                                       |
| richards                | 32.1 ms                                                                  | 24.3 ms: 1.32x faster                                                       |
| mypy2                   | 276 ms                                                                   | 209 ms: 1.32x faster                                                        |
| logging_silent          | 71.0 ns                                                                  | 54.5 ns: 1.30x faster                                                       |
| deepcopy_memo           | 25.3 us                                                                  | 19.6 us: 1.29x faster                                                       |
| unpickle_pure_python    | 150 us                                                                   | 117 us: 1.28x faster                                                        |
| nbody                   | 70.9 ms                                                                  | 55.6 ms: 1.27x faster                                                       |
| raytrace                | 206 ms                                                                   | 164 ms: 1.26x faster                                                        |
| genshi_text             | 17.3 ms                                                                  | 13.8 ms: 1.25x faster                                                       |
| genshi_xml              | 38.0 ms                                                                  | 30.5 ms: 1.25x faster                                                       |
| scimark_lu              | 62.8 ms                                                                  | 50.5 ms: 1.24x faster                                                       |
| mdp                     | 1.67 sec                                                                 | 1.36 sec: 1.23x faster                                                      |
| hexiom                  | 4.46 ms                                                                  | 3.66 ms: 1.22x faster                                                       |
| go                      | 97.5 ms                                                                  | 80.6 ms: 1.21x faster                                                       |
| pickle_pure_python      | 203 us                                                                   | 168 us: 1.21x faster                                                        |
| nqueens                 | 65.1 ms                                                                  | 54.1 ms: 1.20x faster                                                       |
| django_template         | 23.9 ms                                                                  | 19.9 ms: 1.20x faster                                                       |
| chameleon               | 5.15 ms                                                                  | 4.30 ms: 1.20x faster                                                       |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.20 ms: 1.20x faster                                                       |
| chaos                   | 47.3 ms                                                                  | 39.6 ms: 1.20x faster                                                       |
| json                    | 3.20 ms                                                                  | 2.71 ms: 1.18x faster                                                       |
| mako                    | 7.20 ms                                                                  | 6.10 ms: 1.18x faster                                                       |
| spectral_norm           | 71.8 ms                                                                  | 61.1 ms: 1.18x faster                                                       |
| deepcopy                | 240 us                                                                   | 204 us: 1.17x faster                                                        |
| scimark_monte_carlo     | 45.8 ms                                                                  | 39.3 ms: 1.16x faster                                                       |
| pprint_pformat          | 1.05 sec                                                                 | 902 ms: 1.16x faster                                                        |
| float                   | 53.3 ms                                                                  | 46.0 ms: 1.16x faster                                                       |
| pprint_safe_repr        | 512 ms                                                                   | 443 ms: 1.15x faster                                                        |
| scimark_fft             | 183 ms                                                                   | 159 ms: 1.15x faster                                                        |
| fannkuch                | 255 ms                                                                   | 222 ms: 1.15x faster                                                        |
| sqlglot_normalize       | 189 ms                                                                   | 166 ms: 1.14x faster                                                        |
| deepcopy_reduce         | 2.06 us                                                                  | 1.82 us: 1.13x faster                                                       |
| regex_compile           | 89.7 ms                                                                  | 79.6 ms: 1.13x faster                                                       |
| sqlglot_optimize        | 34.5 ms                                                                  | 30.8 ms: 1.12x faster                                                       |
| logging_simple          | 6.60 us                                                                  | 5.91 us: 1.12x faster                                                       |
| pyflate                 | 302 ms                                                                   | 271 ms: 1.11x faster                                                        |
| logging_format          | 7.13 us                                                                  | 6.41 us: 1.11x faster                                                       |
| coverage                | 55.3 ms                                                                  | 50.1 ms: 1.10x faster                                                       |
| sympy_expand            | 298 ms                                                                   | 271 ms: 1.10x faster                                                        |
| sqlglot_parse           | 929 us                                                                   | 843 us: 1.10x faster                                                        |
| scimark_sor             | 77.7 ms                                                                  | 70.6 ms: 1.10x faster                                                       |
| sqlglot_transpile       | 1.13 ms                                                                  | 1.03 ms: 1.09x faster                                                       |
| crypto_pyaes            | 48.3 ms                                                                  | 44.3 ms: 1.09x faster                                                       |
| sympy_str               | 184 ms                                                                   | 169 ms: 1.09x faster                                                        |
| html5lib                | 38.5 ms                                                                  | 35.5 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed | 512 ms                                                                   | 473 ms: 1.08x faster                                                        |
| xml_etree_process       | 36.6 ms                                                                  | 33.9 ms: 1.08x faster                                                       |
| async_tree_memoization  | 374 ms                                                                   | 349 ms: 1.07x faster                                                        |
| pycparser               | 686 ms                                                                   | 640 ms: 1.07x faster                                                        |
| sympy_integrate         | 13.7 ms                                                                  | 12.8 ms: 1.07x faster                                                       |
| coroutines              | 14.8 ms                                                                  | 13.9 ms: 1.06x faster                                                       |
| thrift                  | 487 us                                                                   | 459 us: 1.06x faster                                                        |
| async_tree_none         | 313 ms                                                                   | 295 ms: 1.06x faster                                                        |
| tornado_http            | 91.8 ms                                                                  | 86.7 ms: 1.06x faster                                                       |
| docutils                | 1.59 sec                                                                 | 1.51 sec: 1.06x faster                                                      |
| meteor_contest          | 74.4 ms                                                                  | 70.4 ms: 1.06x faster                                                       |
| xml_etree_parse         | 92.1 ms                                                                  | 87.3 ms: 1.06x faster                                                       |
| 2to3                    | 204 ms                                                                   | 194 ms: 1.05x faster                                                        |
| xml_etree_generate      | 52.3 ms                                                                  | 50.0 ms: 1.05x faster                                                       |
| bench_thread_pool       | 856 us                                                                   | 818 us: 1.05x faster                                                        |
| xml_etree_iterparse     | 61.8 ms                                                                  | 59.2 ms: 1.04x faster                                                       |
| comprehensions          | 15.4 us                                                                  | 14.8 us: 1.04x faster                                                       |
| unpickle_list           | 2.80 us                                                                  | 2.70 us: 1.04x faster                                                       |
| sympy_sum               | 98.9 ms                                                                  | 95.6 ms: 1.03x faster                                                       |
| dulwich_log             | 43.4 ms                                                                  | 42.1 ms: 1.03x faster                                                       |
| async_tree_io           | 744 ms                                                                   | 723 ms: 1.03x faster                                                        |
| telco                   | 3.93 ms                                                                  | 3.85 ms: 1.02x faster                                                       |
| json_loads              | 13.5 us                                                                  | 13.4 us: 1.01x faster                                                       |
| python_startup          | 18.4 ms                                                                  | 18.2 ms: 1.01x faster                                                       |
| unpickle                | 8.01 us                                                                  | 7.96 us: 1.01x faster                                                       |
| pidigits                | 147 ms                                                                   | 146 ms: 1.00x faster                                                        |
| regex_v8                | 13.5 ms                                                                  | 13.8 ms: 1.03x slower                                                       |
| pickle_list             | 2.70 us                                                                  | 2.78 us: 1.03x slower                                                       |
| pickle                  | 6.47 us                                                                  | 6.65 us: 1.03x slower                                                       |
| create_gc_cycles        | 666 us                                                                   | 698 us: 1.05x slower                                                        |
| gc_traversal            | 1.40 ms                                                                  | 1.47 ms: 1.05x slower                                                       |
| sqlite_synth            | 1.67 us                                                                  | 1.76 us: 1.05x slower                                                       |
| regex_dna               | 115 ms                                                                   | 122 ms: 1.06x slower                                                        |
| bench_mp_pool           | 61.2 ms                                                                  | 64.8 ms: 1.06x slower                                                       |
| async_generators        | 180 ms                                                                   | 202 ms: 1.12x slower                                                        |
| regex_effbot            | 1.63 ms                                                                  | 1.83 ms: 1.12x slower                                                       |
| pathlib                 | 72.9 ms                                                                  | 82.2 ms: 1.13x slower                                                       |
| dask                    | 267 ms                                                                   | 353 ms: 1.32x slower                                                        |
| Geometric mean          | (ref)                                                                    | 1.11x faster                                                                |

Benchmark hidden because not significant (2): pickle_dict, python_startup_no_site
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
