
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 2d526cd
- commit date: 2023-05-01
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 207 ms: 1.02x slower                                        |
| html5lib       | 38.5 ms                                                                  | 36.1 ms: 1.06x faster                                       |
| tornado_http   | 91.8 ms                                                                  | 87.3 ms: 1.05x faster                                       |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 67.3 ms: 1.05x faster                                       |
| float          | 53.3 ms                                                                  | 52.2 ms: 1.02x faster                                       |
| pidigits       | 147 ms                                                                   | 148 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 89.7 ms                                                                  | 85.6 ms: 1.05x faster                                       |
| regex_effbot   | 1.63 ms                                                                  | 1.58 ms: 1.03x faster                                       |
| regex_v8       | 13.5 ms                                                                  | 13.6 ms: 1.01x slower                                       |
| regex_dna      | 115 ms                                                                   | 117 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.55 ms: 1.39x faster                                       |
| unpickle_pure_python | 150 us                                                                   | 135 us: 1.11x faster                                        |
| pickle_pure_python   | 203 us                                                                   | 191 us: 1.06x faster                                        |
| pickle_dict          | 18.6 us                                                                  | 18.1 us: 1.03x faster                                       |
| json_loads           | 13.5 us                                                                  | 13.3 us: 1.01x faster                                       |
| xml_etree_process    | 36.6 ms                                                                  | 37.8 ms: 1.03x slower                                       |
| xml_etree_generate   | 52.3 ms                                                                  | 54.6 ms: 1.04x slower                                       |
| pickle_list          | 2.70 us                                                                  | 2.85 us: 1.06x slower                                       |
| pickle               | 6.47 us                                                                  | 7.02 us: 1.09x slower                                       |
| unpickle             | 8.01 us                                                                  | 8.73 us: 1.09x slower                                       |
| Geometric mean       | (ref)                                                                    | 1.02x faster                                                |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup | 18.4 ms                                                                  | 18.3 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_xml     | 38.0 ms                                                                  | 32.5 ms: 1.17x faster                                       |
| genshi_text    | 17.3 ms                                                                  | 14.9 ms: 1.15x faster                                       |
| mako           | 7.20 ms                                                                  | 6.67 ms: 1.08x faster                                       |
| Geometric mean | (ref)                                                                    | 1.13x faster                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|-------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| generators              | 33.5 ms                                                                  | 21.6 ms: 1.56x faster                                       |
| asyncio_tcp             | 674 ms                                                                   | 463 ms: 1.46x faster                                        |
| json_dumps              | 7.71 ms                                                                  | 5.55 ms: 1.39x faster                                       |
| mypy2                   | 276 ms                                                                   | 215 ms: 1.29x faster                                        |
| deltablue               | 2.68 ms                                                                  | 2.12 ms: 1.26x faster                                       |
| richards                | 32.1 ms                                                                  | 25.6 ms: 1.25x faster                                       |
| logging_silent          | 71.0 ns                                                                  | 60.2 ns: 1.18x faster                                       |
| sqlglot_parse           | 929 us                                                                   | 791 us: 1.17x faster                                        |
| genshi_xml              | 38.0 ms                                                                  | 32.5 ms: 1.17x faster                                       |
| mdp                     | 1.67 sec                                                                 | 1.43 sec: 1.17x faster                                      |
| genshi_text             | 17.3 ms                                                                  | 14.9 ms: 1.15x faster                                       |
| go                      | 97.5 ms                                                                  | 86.6 ms: 1.13x faster                                       |
| sqlglot_transpile       | 1.13 ms                                                                  | 1.01 ms: 1.12x faster                                       |
| unpack_sequence         | 43.1 ns                                                                  | 38.7 ns: 1.11x faster                                       |
| unpickle_pure_python    | 150 us                                                                   | 135 us: 1.11x faster                                        |
| scimark_lu              | 62.8 ms                                                                  | 56.8 ms: 1.11x faster                                       |
| hexiom                  | 4.46 ms                                                                  | 4.06 ms: 1.10x faster                                       |
| spectral_norm           | 71.8 ms                                                                  | 65.4 ms: 1.10x faster                                       |
| async_tree_cpu_io_mixed | 512 ms                                                                   | 473 ms: 1.08x faster                                        |
| mako                    | 7.20 ms                                                                  | 6.67 ms: 1.08x faster                                       |
| raytrace                | 206 ms                                                                   | 191 ms: 1.08x faster                                        |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.45 ms: 1.07x faster                                       |
| nqueens                 | 65.1 ms                                                                  | 60.6 ms: 1.07x faster                                       |
| async_tree_memoization  | 374 ms                                                                   | 350 ms: 1.07x faster                                        |
| html5lib                | 38.5 ms                                                                  | 36.1 ms: 1.06x faster                                       |
| fannkuch                | 255 ms                                                                   | 240 ms: 1.06x faster                                        |
| pickle_pure_python      | 203 us                                                                   | 191 us: 1.06x faster                                        |
| json                    | 3.20 ms                                                                  | 3.02 ms: 1.06x faster                                       |
| chaos                   | 47.3 ms                                                                  | 44.6 ms: 1.06x faster                                       |
| deepcopy_memo           | 25.3 us                                                                  | 23.9 us: 1.06x faster                                       |
| coverage                | 55.3 ms                                                                  | 52.3 ms: 1.06x faster                                       |
| async_tree_none         | 313 ms                                                                   | 297 ms: 1.05x faster                                        |
| nbody                   | 70.9 ms                                                                  | 67.3 ms: 1.05x faster                                       |
| tornado_http            | 91.8 ms                                                                  | 87.3 ms: 1.05x faster                                       |
| regex_compile           | 89.7 ms                                                                  | 85.6 ms: 1.05x faster                                       |
| coroutines              | 14.8 ms                                                                  | 14.2 ms: 1.04x faster                                       |
| bench_thread_pool       | 856 us                                                                   | 827 us: 1.03x faster                                        |
| regex_effbot            | 1.63 ms                                                                  | 1.58 ms: 1.03x faster                                       |
| logging_format          | 7.13 us                                                                  | 6.89 us: 1.03x faster                                       |
| pycparser               | 686 ms                                                                   | 665 ms: 1.03x faster                                        |
| pickle_dict             | 18.6 us                                                                  | 18.1 us: 1.03x faster                                       |
| async_tree_io           | 744 ms                                                                   | 724 ms: 1.03x faster                                        |
| deepcopy                | 240 us                                                                   | 233 us: 1.03x faster                                        |
| pprint_pformat          | 1.05 sec                                                                 | 1.02 sec: 1.03x faster                                      |
| pyflate                 | 302 ms                                                                   | 295 ms: 1.02x faster                                        |
| scimark_fft             | 183 ms                                                                   | 179 ms: 1.02x faster                                        |
| float                   | 53.3 ms                                                                  | 52.2 ms: 1.02x faster                                       |
| sqlglot_optimize        | 34.5 ms                                                                  | 33.8 ms: 1.02x faster                                       |
| sqlglot_normalize       | 189 ms                                                                   | 185 ms: 1.02x faster                                        |
| dulwich_log             | 43.4 ms                                                                  | 42.7 ms: 1.02x faster                                       |
| scimark_monte_carlo     | 45.8 ms                                                                  | 45.1 ms: 1.02x faster                                       |
| json_loads              | 13.5 us                                                                  | 13.3 us: 1.01x faster                                       |
| pprint_safe_repr        | 512 ms                                                                   | 505 ms: 1.01x faster                                        |
| logging_simple          | 6.60 us                                                                  | 6.52 us: 1.01x faster                                       |
| python_startup          | 18.4 ms                                                                  | 18.3 ms: 1.01x faster                                       |
| crypto_pyaes            | 48.3 ms                                                                  | 48.1 ms: 1.00x faster                                       |
| regex_v8                | 13.5 ms                                                                  | 13.6 ms: 1.01x slower                                       |
| pidigits                | 147 ms                                                                   | 148 ms: 1.01x slower                                        |
| create_gc_cycles        | 666 us                                                                   | 675 us: 1.01x slower                                        |
| regex_dna               | 115 ms                                                                   | 117 ms: 1.02x slower                                        |
| 2to3                    | 204 ms                                                                   | 207 ms: 1.02x slower                                        |
| scimark_sor             | 77.7 ms                                                                  | 79.1 ms: 1.02x slower                                       |
| comprehensions          | 15.4 us                                                                  | 15.7 us: 1.02x slower                                       |
| sqlite_synth            | 1.67 us                                                                  | 1.71 us: 1.02x slower                                       |
| xml_etree_process       | 36.6 ms                                                                  | 37.8 ms: 1.03x slower                                       |
| meteor_contest          | 74.4 ms                                                                  | 77.0 ms: 1.04x slower                                       |
| telco                   | 3.93 ms                                                                  | 4.07 ms: 1.04x slower                                       |
| gc_traversal            | 1.40 ms                                                                  | 1.46 ms: 1.04x slower                                       |
| thrift                  | 487 us                                                                   | 508 us: 1.04x slower                                        |
| xml_etree_generate      | 52.3 ms                                                                  | 54.6 ms: 1.04x slower                                       |
| pickle_list             | 2.70 us                                                                  | 2.85 us: 1.06x slower                                       |
| pickle                  | 6.47 us                                                                  | 7.02 us: 1.09x slower                                       |
| unpickle                | 8.01 us                                                                  | 8.73 us: 1.09x slower                                       |
| bench_mp_pool           | 61.2 ms                                                                  | 67.2 ms: 1.10x slower                                       |
| pathlib                 | 72.9 ms                                                                  | 83.1 ms: 1.14x slower                                       |
| async_generators        | 180 ms                                                                   | 227 ms: 1.26x slower                                        |
| dask                    | 267 ms                                                                   | 360 ms: 1.35x slower                                        |
| Geometric mean          | (ref)                                                                    | 1.04x faster                                                |

Benchmark hidden because not significant (6): xml_etree_iterparse, xml_etree_parse, docutils, unpickle_list, python_startup_no_site, deepcopy_reduce
Ignored benchmarks (11) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum
