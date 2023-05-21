
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 99b6418
- commit date: 2023-05-21
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-pythonperf1-amd64-python-main-3.12.0a7+-99b6418 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.62 sec: 1.01x slower                                      |
| tornado_http   | 91.8 ms                                                     | 89.3 ms: 1.03x faster                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-pythonperf1-amd64-python-main-3.12.0a7+-99b6418 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 54.6 ms                                                     | 53.6 ms: 1.02x faster                                       |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                       | 1.00x slower                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-pythonperf1-amd64-python-main-3.12.0a7+-99b6418 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 86.3 ms: 1.05x faster                                       |
| regex_v8       | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                       |
| regex_dna      | 115 ms                                                      | 125 ms: 1.08x slower                                        |
| regex_effbot   | 1.50 ms                                                     | 1.66 ms: 1.11x slower                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-pythonperf1-amd64-python-main-3.12.0a7+-99b6418 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.59 ms: 1.35x faster                                       |
| unpickle_pure_python | 152 us                                                      | 132 us: 1.15x faster                                        |
| tomli_loads          | 1.41 sec                                                    | 1.34 sec: 1.06x faster                                      |
| pickle_pure_python   | 200 us                                                      | 193 us: 1.03x faster                                        |
| pickle_dict          | 18.5 us                                                     | 18.1 us: 1.02x faster                                       |
| xml_etree_parse      | 95.9 ms                                                     | 94.7 ms: 1.01x faster                                       |
| xml_etree_process    | 37.1 ms                                                     | 37.9 ms: 1.02x slower                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.5 ms: 1.05x slower                                       |
| pickle               | 6.61 us                                                     | 6.95 us: 1.05x slower                                       |
| unpickle             | 8.09 us                                                     | 8.53 us: 1.05x slower                                       |
| json_loads           | 12.9 us                                                     | 13.8 us: 1.07x slower                                       |
| xml_etree_generate   | 52.2 ms                                                     | 56.0 ms: 1.07x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.88 us: 1.07x slower                                       |
| unpickle_list        | 2.55 us                                                     | 3.02 us: 1.19x slower                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-pythonperf1-amd64-python-main-3.12.0a7+-99b6418 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.3 ms: 1.03x slower                                       |
| python_startup         | 18.7 ms                                                     | 19.3 ms: 1.03x slower                                       |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-pythonperf1-amd64-python-main-3.12.0a7+-99b6418 |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.61 ms: 1.10x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-pythonperf1-amd64-python-main-3.12.0a7+-99b6418 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 91.7 us: 3.51x faster                                       |
| generators               | 33.8 ms                                                     | 21.5 ms: 1.57x faster                                       |
| json_dumps               | 7.56 ms                                                     | 5.59 ms: 1.35x faster                                       |
| richards_super           | 37.5 ms                                                     | 29.3 ms: 1.28x faster                                       |
| mdp                      | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                      |
| deltablue                | 2.61 ms                                                     | 2.13 ms: 1.23x faster                                       |
| unpack_sequence          | 46.1 ns                                                     | 37.8 ns: 1.22x faster                                       |
| asyncio_tcp              | 699 ms                                                      | 582 ms: 1.20x faster                                        |
| sqlglot_parse            | 952 us                                                      | 796 us: 1.20x faster                                        |
| richards                 | 30.6 ms                                                     | 25.7 ms: 1.19x faster                                       |
| logging_silent           | 69.8 ns                                                     | 60.1 ns: 1.16x faster                                       |
| hexiom                   | 4.55 ms                                                     | 3.95 ms: 1.15x faster                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 1.01 ms: 1.15x faster                                       |
| unpickle_pure_python     | 152 us                                                      | 132 us: 1.15x faster                                        |
| async_tree_none          | 320 ms                                                      | 282 ms: 1.13x faster                                        |
| comprehensions           | 15.9 us                                                     | 14.1 us: 1.13x faster                                       |
| raytrace                 | 211 ms                                                      | 187 ms: 1.13x faster                                        |
| async_tree_io            | 779 ms                                                      | 700 ms: 1.11x faster                                        |
| go                       | 97.3 ms                                                     | 87.7 ms: 1.11x faster                                       |
| coverage                 | 55.9 ms                                                     | 50.4 ms: 1.11x faster                                       |
| async_tree_memoization   | 371 ms                                                      | 335 ms: 1.11x faster                                        |
| json                     | 3.25 ms                                                     | 2.95 ms: 1.10x faster                                       |
| deepcopy_memo            | 25.2 us                                                     | 22.9 us: 1.10x faster                                       |
| mako                     | 7.26 ms                                                     | 6.61 ms: 1.10x faster                                       |
| scimark_lu               | 63.5 ms                                                     | 58.5 ms: 1.09x faster                                       |
| nqueens                  | 64.9 ms                                                     | 60.2 ms: 1.08x faster                                       |
| pyflate                  | 304 ms                                                      | 284 ms: 1.07x faster                                        |
| mypy2                    | 229 ms                                                      | 215 ms: 1.07x faster                                        |
| deepcopy                 | 246 us                                                      | 230 us: 1.07x faster                                        |
| chaos                    | 47.1 ms                                                     | 44.4 ms: 1.06x faster                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 474 ms: 1.06x faster                                        |
| tomli_loads              | 1.41 sec                                                    | 1.34 sec: 1.06x faster                                      |
| coroutines               | 14.6 ms                                                     | 13.9 ms: 1.06x faster                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.00 sec: 1.05x faster                                      |
| regex_compile            | 90.6 ms                                                     | 86.3 ms: 1.05x faster                                       |
| spectral_norm            | 67.9 ms                                                     | 64.8 ms: 1.05x faster                                       |
| scimark_monte_carlo      | 44.6 ms                                                     | 42.6 ms: 1.05x faster                                       |
| sqlglot_normalize        | 190 ms                                                      | 182 ms: 1.04x faster                                        |
| fannkuch                 | 252 ms                                                      | 242 ms: 1.04x faster                                        |
| dulwich_log              | 44.5 ms                                                     | 42.9 ms: 1.04x faster                                       |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.48 ms: 1.03x faster                                       |
| pickle_pure_python       | 200 us                                                      | 193 us: 1.03x faster                                        |
| meteor_contest           | 74.7 ms                                                     | 72.3 ms: 1.03x faster                                       |
| tornado_http             | 91.8 ms                                                     | 89.3 ms: 1.03x faster                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 34.0 ms: 1.03x faster                                       |
| pycparser                | 691 ms                                                      | 673 ms: 1.03x faster                                        |
| pickle_dict              | 18.5 us                                                     | 18.1 us: 1.02x faster                                       |
| bench_thread_pool        | 852 us                                                      | 834 us: 1.02x faster                                        |
| float                    | 54.6 ms                                                     | 53.6 ms: 1.02x faster                                       |
| pprint_pformat           | 1.04 sec                                                    | 1.02 sec: 1.02x faster                                      |
| aiohttp                  | 899 us                                                      | 886 us: 1.01x faster                                        |
| scimark_fft              | 178 ms                                                      | 176 ms: 1.01x faster                                        |
| xml_etree_parse          | 95.9 ms                                                     | 94.7 ms: 1.01x faster                                       |
| gc_traversal             | 1.46 ms                                                     | 1.45 ms: 1.01x faster                                       |
| logging_simple           | 6.61 us                                                     | 6.57 us: 1.01x faster                                       |
| sqlite_synth             | 1.68 us                                                     | 1.69 us: 1.01x slower                                       |
| docutils                 | 1.60 sec                                                    | 1.62 sec: 1.01x slower                                      |
| crypto_pyaes             | 47.6 ms                                                     | 48.0 ms: 1.01x slower                                       |
| logging_format           | 7.01 us                                                     | 7.09 us: 1.01x slower                                       |
| deepcopy_reduce          | 2.07 us                                                     | 2.10 us: 1.01x slower                                       |
| pidigits                 | 148 ms                                                      | 151 ms: 1.02x slower                                        |
| regex_v8                 | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                       |
| xml_etree_process        | 37.1 ms                                                     | 37.9 ms: 1.02x slower                                       |
| python_startup_no_site   | 15.9 ms                                                     | 16.3 ms: 1.03x slower                                       |
| python_startup           | 18.7 ms                                                     | 19.3 ms: 1.03x slower                                       |
| scimark_sor              | 75.6 ms                                                     | 78.9 ms: 1.04x slower                                       |
| telco                    | 3.90 ms                                                     | 4.08 ms: 1.05x slower                                       |
| xml_etree_iterparse      | 62.6 ms                                                     | 65.5 ms: 1.05x slower                                       |
| pickle                   | 6.61 us                                                     | 6.95 us: 1.05x slower                                       |
| unpickle                 | 8.09 us                                                     | 8.53 us: 1.05x slower                                       |
| json_loads               | 12.9 us                                                     | 13.8 us: 1.07x slower                                       |
| xml_etree_generate       | 52.2 ms                                                     | 56.0 ms: 1.07x slower                                       |
| pickle_list              | 2.68 us                                                     | 2.88 us: 1.07x slower                                       |
| regex_dna                | 115 ms                                                      | 125 ms: 1.08x slower                                        |
| bench_mp_pool            | 62.5 ms                                                     | 68.4 ms: 1.09x slower                                       |
| regex_effbot             | 1.50 ms                                                     | 1.66 ms: 1.11x slower                                       |
| unpickle_list            | 2.55 us                                                     | 3.02 us: 1.19x slower                                       |
| pathlib                  | 71.4 ms                                                     | 85.3 ms: 1.20x slower                                       |
| async_generators         | 178 ms                                                      | 231 ms: 1.30x slower                                        |
| dask                     | 264 ms                                                      | 366 ms: 1.38x slower                                        |
| Geometric mean           | (ref)                                                       | 1.05x faster                                                |

Benchmark hidden because not significant (4): pprint_safe_repr, 2to3, create_gc_cycles, nbody
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
