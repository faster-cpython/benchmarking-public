
# Results vs. 3.11.0

- fork: faster-cpython
- ref: no_predict
- machine: windows-amd64
- commit hash: f190abf
- commit date: 2023-05-12
- overall geometric mean: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 206 ms: 1.01x faster                                                        |
| tornado_http   | 91.8 ms                                                     | 89.5 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 51.6 ms: 1.06x faster                                                       |
| nbody          | 70.0 ms                                                     | 68.3 ms: 1.02x faster                                                       |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 84.2 ms: 1.08x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                                       |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.59 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.69 ms: 1.33x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 130 us: 1.17x faster                                                        |
| tomli_loads          | 1.41 sec                                                    | 1.32 sec: 1.08x faster                                                      |
| pickle_pure_python   | 200 us                                                      | 187 us: 1.07x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 90.3 ms: 1.06x faster                                                       |
| unpickle             | 8.09 us                                                     | 8.04 us: 1.01x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 37.6 ms: 1.01x slower                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 54.8 ms: 1.05x slower                                                       |
| json_loads           | 12.9 us                                                     | 13.7 us: 1.06x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.85 us: 1.06x slower                                                       |
| pickle               | 6.61 us                                                     | 7.18 us: 1.09x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.90 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (2): pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.2 ms: 1.02x slower                                                       |
| python_startup         | 18.7 ms                                                     | 19.2 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.53 ms: 1.11x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 95.3 us: 3.38x faster                                                       |
| generators               | 33.8 ms                                                     | 21.5 ms: 1.57x faster                                                       |
| asyncio_tcp              | 699 ms                                                      | 483 ms: 1.45x faster                                                        |
| json_dumps               | 7.56 ms                                                     | 5.69 ms: 1.33x faster                                                       |
| richards_super           | 37.5 ms                                                     | 28.6 ms: 1.31x faster                                                       |
| deltablue                | 2.61 ms                                                     | 2.07 ms: 1.26x faster                                                       |
| unpack_sequence          | 46.1 ns                                                     | 37.5 ns: 1.23x faster                                                       |
| sqlglot_parse            | 952 us                                                      | 784 us: 1.21x faster                                                        |
| richards                 | 30.6 ms                                                     | 25.2 ms: 1.21x faster                                                       |
| logging_silent           | 69.8 ns                                                     | 58.6 ns: 1.19x faster                                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 983 us: 1.18x faster                                                        |
| hexiom                   | 4.55 ms                                                     | 3.86 ms: 1.18x faster                                                       |
| mdp                      | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                      |
| unpickle_pure_python     | 152 us                                                      | 130 us: 1.17x faster                                                        |
| go                       | 97.3 ms                                                     | 85.0 ms: 1.15x faster                                                       |
| raytrace                 | 211 ms                                                      | 184 ms: 1.14x faster                                                        |
| async_tree_none          | 320 ms                                                      | 282 ms: 1.14x faster                                                        |
| comprehensions           | 15.9 us                                                     | 14.1 us: 1.13x faster                                                       |
| async_tree_memoization   | 371 ms                                                      | 329 ms: 1.13x faster                                                        |
| scimark_lu               | 63.5 ms                                                     | 56.5 ms: 1.12x faster                                                       |
| mako                     | 7.26 ms                                                     | 6.53 ms: 1.11x faster                                                       |
| deepcopy_memo            | 25.2 us                                                     | 22.8 us: 1.10x faster                                                       |
| json                     | 3.25 ms                                                     | 2.97 ms: 1.09x faster                                                       |
| chaos                    | 47.1 ms                                                     | 43.1 ms: 1.09x faster                                                       |
| spectral_norm            | 67.9 ms                                                     | 62.1 ms: 1.09x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.94 sec: 1.09x faster                                                      |
| async_tree_io            | 779 ms                                                      | 719 ms: 1.08x faster                                                        |
| scimark_monte_carlo      | 44.6 ms                                                     | 41.3 ms: 1.08x faster                                                       |
| nqueens                  | 64.9 ms                                                     | 60.1 ms: 1.08x faster                                                       |
| mypy2                    | 229 ms                                                      | 213 ms: 1.08x faster                                                        |
| regex_compile            | 90.6 ms                                                     | 84.2 ms: 1.08x faster                                                       |
| coverage                 | 55.9 ms                                                     | 52.0 ms: 1.08x faster                                                       |
| tomli_loads              | 1.41 sec                                                    | 1.32 sec: 1.08x faster                                                      |
| deepcopy                 | 246 us                                                      | 229 us: 1.07x faster                                                        |
| fannkuch                 | 252 ms                                                      | 235 ms: 1.07x faster                                                        |
| pickle_pure_python       | 200 us                                                      | 187 us: 1.07x faster                                                        |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.41 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 470 ms: 1.07x faster                                                        |
| xml_etree_parse          | 95.9 ms                                                     | 90.3 ms: 1.06x faster                                                       |
| pyflate                  | 304 ms                                                      | 286 ms: 1.06x faster                                                        |
| float                    | 54.6 ms                                                     | 51.6 ms: 1.06x faster                                                       |
| scimark_fft              | 178 ms                                                      | 170 ms: 1.05x faster                                                        |
| coroutines               | 14.6 ms                                                     | 14.0 ms: 1.05x faster                                                       |
| sqlglot_normalize        | 190 ms                                                      | 182 ms: 1.04x faster                                                        |
| dulwich_log              | 44.5 ms                                                     | 42.7 ms: 1.04x faster                                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 33.6 ms: 1.04x faster                                                       |
| meteor_contest           | 74.7 ms                                                     | 72.3 ms: 1.03x faster                                                       |
| bench_thread_pool        | 852 us                                                      | 826 us: 1.03x faster                                                        |
| logging_simple           | 6.61 us                                                     | 6.44 us: 1.03x faster                                                       |
| tornado_http             | 91.8 ms                                                     | 89.5 ms: 1.03x faster                                                       |
| deepcopy_reduce          | 2.07 us                                                     | 2.02 us: 1.03x faster                                                       |
| nbody                    | 70.0 ms                                                     | 68.3 ms: 1.02x faster                                                       |
| pycparser                | 691 ms                                                      | 675 ms: 1.02x faster                                                        |
| pprint_safe_repr         | 512 ms                                                      | 501 ms: 1.02x faster                                                        |
| pprint_pformat           | 1.04 sec                                                    | 1.03 sec: 1.01x faster                                                      |
| 2to3                     | 209 ms                                                      | 206 ms: 1.01x faster                                                        |
| aiohttp                  | 899 us                                                      | 889 us: 1.01x faster                                                        |
| unpickle                 | 8.09 us                                                     | 8.04 us: 1.01x faster                                                       |
| crypto_pyaes             | 47.6 ms                                                     | 47.3 ms: 1.01x faster                                                       |
| gc_traversal             | 1.46 ms                                                     | 1.47 ms: 1.01x slower                                                       |
| create_gc_cycles         | 693 us                                                      | 702 us: 1.01x slower                                                        |
| xml_etree_process        | 37.1 ms                                                     | 37.6 ms: 1.01x slower                                                       |
| pidigits                 | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| regex_v8                 | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                                       |
| sqlite_synth             | 1.68 us                                                     | 1.71 us: 1.02x slower                                                       |
| python_startup_no_site   | 15.9 ms                                                     | 16.2 ms: 1.02x slower                                                       |
| python_startup           | 18.7 ms                                                     | 19.2 ms: 1.03x slower                                                       |
| scimark_sor              | 75.6 ms                                                     | 77.6 ms: 1.03x slower                                                       |
| regex_dna                | 115 ms                                                      | 120 ms: 1.04x slower                                                        |
| telco                    | 3.90 ms                                                     | 4.08 ms: 1.05x slower                                                       |
| xml_etree_generate       | 52.2 ms                                                     | 54.8 ms: 1.05x slower                                                       |
| json_loads               | 12.9 us                                                     | 13.7 us: 1.06x slower                                                       |
| pickle_list              | 2.68 us                                                     | 2.85 us: 1.06x slower                                                       |
| regex_effbot             | 1.50 ms                                                     | 1.59 ms: 1.06x slower                                                       |
| bench_mp_pool            | 62.5 ms                                                     | 67.0 ms: 1.07x slower                                                       |
| pickle                   | 6.61 us                                                     | 7.18 us: 1.09x slower                                                       |
| unpickle_list            | 2.55 us                                                     | 2.90 us: 1.14x slower                                                       |
| pathlib                  | 71.4 ms                                                     | 81.8 ms: 1.15x slower                                                       |
| async_generators         | 178 ms                                                      | 234 ms: 1.32x slower                                                        |
| dask                     | 264 ms                                                      | 361 ms: 1.37x slower                                                        |
| Geometric mean           | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (4): pickle_dict, logging_format, xml_etree_iterparse, docutils
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
