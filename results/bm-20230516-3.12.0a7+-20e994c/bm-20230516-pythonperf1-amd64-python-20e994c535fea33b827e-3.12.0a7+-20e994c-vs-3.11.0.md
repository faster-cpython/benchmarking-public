
# Results vs. 3.11.0

- fork: python
- ref: 20e994c535fea33b827e
- machine: windows-amd64
- commit hash: 20e994c
- commit date: 2023-05-16
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 214 ms: 1.02x slower                                                        |
| tornado_http   | 91.8 ms                                                     | 88.4 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 55.9 ms: 1.02x slower                                                       |
| nbody          | 70.0 ms                                                     | 76.5 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 87.4 ms: 1.04x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 13.7 ms: 1.01x faster                                                       |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.59 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.82 ms: 1.30x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 138 us: 1.10x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 93.0 ms: 1.03x faster                                                       |
| pickle_dict          | 18.5 us                                                     | 18.1 us: 1.02x faster                                                       |
| pickle_pure_python   | 200 us                                                      | 198 us: 1.01x faster                                                        |
| tomli_loads          | 1.41 sec                                                    | 1.43 sec: 1.01x slower                                                      |
| unpickle             | 8.09 us                                                     | 8.33 us: 1.03x slower                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.8 ms: 1.05x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.85 us: 1.06x slower                                                       |
| json_loads           | 12.9 us                                                     | 13.7 us: 1.06x slower                                                       |
| pickle               | 6.61 us                                                     | 7.15 us: 1.08x slower                                                       |
| xml_etree_process    | 37.1 ms                                                     | 40.2 ms: 1.08x slower                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 57.2 ms: 1.10x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.88 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.3 ms: 1.03x slower                                                       |
| python_startup         | 18.7 ms                                                     | 19.2 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.92 ms: 1.05x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 105 us: 3.07x faster                                                        |
| generators               | 33.8 ms                                                     | 22.9 ms: 1.48x faster                                                       |
| asyncio_tcp              | 699 ms                                                      | 486 ms: 1.44x faster                                                        |
| json_dumps               | 7.56 ms                                                     | 5.82 ms: 1.30x faster                                                       |
| richards_super           | 37.5 ms                                                     | 31.2 ms: 1.20x faster                                                       |
| deltablue                | 2.61 ms                                                     | 2.21 ms: 1.18x faster                                                       |
| mdp                      | 1.67 sec                                                    | 1.45 sec: 1.15x faster                                                      |
| logging_silent           | 69.8 ns                                                     | 60.9 ns: 1.15x faster                                                       |
| sqlglot_parse            | 952 us                                                      | 834 us: 1.14x faster                                                        |
| async_tree_none          | 320 ms                                                      | 286 ms: 1.12x faster                                                        |
| async_tree_memoization   | 371 ms                                                      | 331 ms: 1.12x faster                                                        |
| richards                 | 30.6 ms                                                     | 27.4 ms: 1.12x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.89 sec: 1.11x faster                                                      |
| unpack_sequence          | 46.1 ns                                                     | 41.4 ns: 1.11x faster                                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 1.05 ms: 1.11x faster                                                       |
| coverage                 | 55.9 ms                                                     | 50.4 ms: 1.11x faster                                                       |
| raytrace                 | 211 ms                                                      | 191 ms: 1.10x faster                                                        |
| unpickle_pure_python     | 152 us                                                      | 138 us: 1.10x faster                                                        |
| comprehensions           | 15.9 us                                                     | 14.6 us: 1.09x faster                                                       |
| go                       | 97.3 ms                                                     | 89.4 ms: 1.09x faster                                                       |
| async_tree_io            | 779 ms                                                      | 718 ms: 1.08x faster                                                        |
| json                     | 3.25 ms                                                     | 3.02 ms: 1.08x faster                                                       |
| scimark_lu               | 63.5 ms                                                     | 59.2 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 471 ms: 1.06x faster                                                        |
| mypy2                    | 229 ms                                                      | 215 ms: 1.06x faster                                                        |
| chaos                    | 47.1 ms                                                     | 44.4 ms: 1.06x faster                                                       |
| hexiom                   | 4.55 ms                                                     | 4.31 ms: 1.06x faster                                                       |
| dulwich_log              | 44.5 ms                                                     | 42.4 ms: 1.05x faster                                                       |
| mako                     | 7.26 ms                                                     | 6.92 ms: 1.05x faster                                                       |
| spectral_norm            | 67.9 ms                                                     | 65.0 ms: 1.05x faster                                                       |
| nqueens                  | 64.9 ms                                                     | 62.2 ms: 1.04x faster                                                       |
| tornado_http             | 91.8 ms                                                     | 88.4 ms: 1.04x faster                                                       |
| regex_compile            | 90.6 ms                                                     | 87.4 ms: 1.04x faster                                                       |
| sqlglot_normalize        | 190 ms                                                      | 184 ms: 1.03x faster                                                        |
| xml_etree_parse          | 95.9 ms                                                     | 93.0 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.50 ms: 1.03x faster                                                       |
| fannkuch                 | 252 ms                                                      | 245 ms: 1.03x faster                                                        |
| pickle_dict              | 18.5 us                                                     | 18.1 us: 1.02x faster                                                       |
| deepcopy                 | 246 us                                                      | 242 us: 1.02x faster                                                        |
| regex_v8                 | 13.8 ms                                                     | 13.7 ms: 1.01x faster                                                       |
| pickle_pure_python       | 200 us                                                      | 198 us: 1.01x faster                                                        |
| meteor_contest           | 74.7 ms                                                     | 75.1 ms: 1.00x slower                                                       |
| logging_simple           | 6.61 us                                                     | 6.65 us: 1.01x slower                                                       |
| sqlite_synth             | 1.68 us                                                     | 1.70 us: 1.01x slower                                                       |
| crypto_pyaes             | 47.6 ms                                                     | 48.0 ms: 1.01x slower                                                       |
| gc_traversal             | 1.46 ms                                                     | 1.47 ms: 1.01x slower                                                       |
| tomli_loads              | 1.41 sec                                                    | 1.43 sec: 1.01x slower                                                      |
| logging_format           | 7.01 us                                                     | 7.11 us: 1.01x slower                                                       |
| regex_dna                | 115 ms                                                      | 118 ms: 1.02x slower                                                        |
| 2to3                     | 209 ms                                                      | 214 ms: 1.02x slower                                                        |
| float                    | 54.6 ms                                                     | 55.9 ms: 1.02x slower                                                       |
| python_startup_no_site   | 15.9 ms                                                     | 16.3 ms: 1.03x slower                                                       |
| telco                    | 3.90 ms                                                     | 4.02 ms: 1.03x slower                                                       |
| unpickle                 | 8.09 us                                                     | 8.33 us: 1.03x slower                                                       |
| python_startup           | 18.7 ms                                                     | 19.2 ms: 1.03x slower                                                       |
| deepcopy_reduce          | 2.07 us                                                     | 2.16 us: 1.04x slower                                                       |
| scimark_fft              | 178 ms                                                      | 187 ms: 1.05x slower                                                        |
| xml_etree_iterparse      | 62.6 ms                                                     | 65.8 ms: 1.05x slower                                                       |
| pprint_safe_repr         | 512 ms                                                      | 539 ms: 1.05x slower                                                        |
| pprint_pformat           | 1.04 sec                                                    | 1.10 sec: 1.06x slower                                                      |
| pickle_list              | 2.68 us                                                     | 2.85 us: 1.06x slower                                                       |
| json_loads               | 12.9 us                                                     | 13.7 us: 1.06x slower                                                       |
| regex_effbot             | 1.50 ms                                                     | 1.59 ms: 1.07x slower                                                       |
| pickle                   | 6.61 us                                                     | 7.15 us: 1.08x slower                                                       |
| xml_etree_process        | 37.1 ms                                                     | 40.2 ms: 1.08x slower                                                       |
| bench_mp_pool            | 62.5 ms                                                     | 67.9 ms: 1.09x slower                                                       |
| nbody                    | 70.0 ms                                                     | 76.5 ms: 1.09x slower                                                       |
| xml_etree_generate       | 52.2 ms                                                     | 57.2 ms: 1.10x slower                                                       |
| scimark_sor              | 75.6 ms                                                     | 85.1 ms: 1.13x slower                                                       |
| unpickle_list            | 2.55 us                                                     | 2.88 us: 1.13x slower                                                       |
| pathlib                  | 71.4 ms                                                     | 82.0 ms: 1.15x slower                                                       |
| async_generators         | 178 ms                                                      | 235 ms: 1.32x slower                                                        |
| dask                     | 264 ms                                                      | 364 ms: 1.38x slower                                                        |
| Geometric mean           | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (11): coroutines, sqlglot_optimize, deepcopy_memo, scimark_monte_carlo, pycparser, bench_thread_pool, pyflate, pidigits, aiohttp, docutils, create_gc_cycles
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
