
# Results vs. 3.11.0

- fork: python
- ref: f7df17394906f2af51af
- machine: windows-amd64
- commit hash: f7df173
- commit date: 2023-05-17
- overall geometric mean: 1.06x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 211 ms: 1.01x slower                                                        |
| docutils       | 1.60 sec                                                    | 1.62 sec: 1.01x slower                                                      |
| tornado_http   | 91.8 ms                                                     | 89.5 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 69.1 ms: 1.01x faster                                                       |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 85.5 ms: 1.06x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                        |
| regex_v8       | 13.8 ms                                                     | 14.3 ms: 1.03x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.51 ms: 1.37x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 131 us: 1.16x faster                                                        |
| tomli_loads          | 1.41 sec                                                    | 1.33 sec: 1.06x faster                                                      |
| xml_etree_parse      | 95.9 ms                                                     | 91.5 ms: 1.05x faster                                                       |
| pickle_pure_python   | 200 us                                                      | 191 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.6 ms: 1.02x slower                                                       |
| xml_etree_process    | 37.1 ms                                                     | 38.1 ms: 1.03x slower                                                       |
| json_loads           | 12.9 us                                                     | 13.3 us: 1.03x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.86 us: 1.07x slower                                                       |
| pickle               | 6.61 us                                                     | 7.12 us: 1.08x slower                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 56.7 ms: 1.09x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.78 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.4 ms: 1.03x slower                                                       |
| python_startup         | 18.7 ms                                                     | 19.5 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.61 ms: 1.10x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 99.4 us: 3.24x faster                                                       |
| generators               | 33.8 ms                                                     | 21.5 ms: 1.57x faster                                                       |
| asyncio_tcp              | 699 ms                                                      | 470 ms: 1.49x faster                                                        |
| json_dumps               | 7.56 ms                                                     | 5.51 ms: 1.37x faster                                                       |
| richards_super           | 37.5 ms                                                     | 29.4 ms: 1.27x faster                                                       |
| deltablue                | 2.61 ms                                                     | 2.07 ms: 1.26x faster                                                       |
| richards                 | 30.6 ms                                                     | 25.5 ms: 1.20x faster                                                       |
| sqlglot_parse            | 952 us                                                      | 794 us: 1.20x faster                                                        |
| mdp                      | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                      |
| hexiom                   | 4.55 ms                                                     | 3.93 ms: 1.16x faster                                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 1.01 ms: 1.16x faster                                                       |
| unpickle_pure_python     | 152 us                                                      | 131 us: 1.16x faster                                                        |
| logging_silent           | 69.8 ns                                                     | 60.7 ns: 1.15x faster                                                       |
| comprehensions           | 15.9 us                                                     | 14.0 us: 1.13x faster                                                       |
| scimark_lu               | 63.5 ms                                                     | 56.3 ms: 1.13x faster                                                       |
| unpack_sequence          | 46.1 ns                                                     | 40.8 ns: 1.13x faster                                                       |
| raytrace                 | 211 ms                                                      | 188 ms: 1.12x faster                                                        |
| go                       | 97.3 ms                                                     | 86.8 ms: 1.12x faster                                                       |
| json                     | 3.25 ms                                                     | 2.92 ms: 1.12x faster                                                       |
| async_tree_none          | 320 ms                                                      | 288 ms: 1.11x faster                                                        |
| coverage                 | 55.9 ms                                                     | 50.3 ms: 1.11x faster                                                       |
| async_tree_memoization   | 371 ms                                                      | 336 ms: 1.10x faster                                                        |
| mako                     | 7.26 ms                                                     | 6.61 ms: 1.10x faster                                                       |
| deepcopy_memo            | 25.2 us                                                     | 23.1 us: 1.09x faster                                                       |
| async_tree_io            | 779 ms                                                      | 720 ms: 1.08x faster                                                        |
| chaos                    | 47.1 ms                                                     | 43.7 ms: 1.08x faster                                                       |
| mypy2                    | 229 ms                                                      | 213 ms: 1.08x faster                                                        |
| nqueens                  | 64.9 ms                                                     | 60.4 ms: 1.07x faster                                                       |
| dulwich_log              | 44.5 ms                                                     | 41.8 ms: 1.06x faster                                                       |
| coroutines               | 14.6 ms                                                     | 13.8 ms: 1.06x faster                                                       |
| deepcopy                 | 246 us                                                      | 231 us: 1.06x faster                                                        |
| tomli_loads              | 1.41 sec                                                    | 1.33 sec: 1.06x faster                                                      |
| regex_compile            | 90.6 ms                                                     | 85.5 ms: 1.06x faster                                                       |
| spectral_norm            | 67.9 ms                                                     | 64.3 ms: 1.06x faster                                                       |
| pyflate                  | 304 ms                                                      | 289 ms: 1.05x faster                                                        |
| xml_etree_parse          | 95.9 ms                                                     | 91.5 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 478 ms: 1.05x faster                                                        |
| pickle_pure_python       | 200 us                                                      | 191 us: 1.05x faster                                                        |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.46 ms: 1.05x faster                                                       |
| sqlglot_normalize        | 190 ms                                                      | 183 ms: 1.04x faster                                                        |
| pycparser                | 691 ms                                                      | 669 ms: 1.03x faster                                                        |
| fannkuch                 | 252 ms                                                      | 245 ms: 1.03x faster                                                        |
| deepcopy_reduce          | 2.07 us                                                     | 2.01 us: 1.03x faster                                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 33.9 ms: 1.03x faster                                                       |
| tornado_http             | 91.8 ms                                                     | 89.5 ms: 1.03x faster                                                       |
| logging_format           | 7.01 us                                                     | 6.85 us: 1.02x faster                                                       |
| scimark_monte_carlo      | 44.6 ms                                                     | 43.6 ms: 1.02x faster                                                       |
| meteor_contest           | 74.7 ms                                                     | 73.3 ms: 1.02x faster                                                       |
| bench_thread_pool        | 852 us                                                      | 838 us: 1.02x faster                                                        |
| logging_simple           | 6.61 us                                                     | 6.52 us: 1.01x faster                                                       |
| nbody                    | 70.0 ms                                                     | 69.1 ms: 1.01x faster                                                       |
| aiohttp                  | 899 us                                                      | 891 us: 1.01x faster                                                        |
| crypto_pyaes             | 47.6 ms                                                     | 47.1 ms: 1.01x faster                                                       |
| docutils                 | 1.60 sec                                                    | 1.62 sec: 1.01x slower                                                      |
| 2to3                     | 209 ms                                                      | 211 ms: 1.01x slower                                                        |
| regex_dna                | 115 ms                                                      | 117 ms: 1.01x slower                                                        |
| sqlite_synth             | 1.68 us                                                     | 1.71 us: 1.02x slower                                                       |
| pidigits                 | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| xml_etree_iterparse      | 62.6 ms                                                     | 63.6 ms: 1.02x slower                                                       |
| gc_traversal             | 1.46 ms                                                     | 1.49 ms: 1.02x slower                                                       |
| xml_etree_process        | 37.1 ms                                                     | 38.1 ms: 1.03x slower                                                       |
| json_loads               | 12.9 us                                                     | 13.3 us: 1.03x slower                                                       |
| python_startup_no_site   | 15.9 ms                                                     | 16.4 ms: 1.03x slower                                                       |
| regex_v8                 | 13.8 ms                                                     | 14.3 ms: 1.03x slower                                                       |
| python_startup           | 18.7 ms                                                     | 19.5 ms: 1.04x slower                                                       |
| telco                    | 3.90 ms                                                     | 4.08 ms: 1.04x slower                                                       |
| pickle_list              | 2.68 us                                                     | 2.86 us: 1.07x slower                                                       |
| regex_effbot             | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| pickle                   | 6.61 us                                                     | 7.12 us: 1.08x slower                                                       |
| bench_mp_pool            | 62.5 ms                                                     | 67.5 ms: 1.08x slower                                                       |
| scimark_sor              | 75.6 ms                                                     | 81.6 ms: 1.08x slower                                                       |
| xml_etree_generate       | 52.2 ms                                                     | 56.7 ms: 1.09x slower                                                       |
| unpickle_list            | 2.55 us                                                     | 2.78 us: 1.09x slower                                                       |
| pathlib                  | 71.4 ms                                                     | 83.0 ms: 1.16x slower                                                       |
| async_generators         | 178 ms                                                      | 225 ms: 1.27x slower                                                        |
| dask                     | 264 ms                                                      | 364 ms: 1.38x slower                                                        |
| Geometric mean           | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (8): asyncio_tcp_ssl, float, pprint_pformat, pprint_safe_repr, scimark_fft, unpickle, pickle_dict, create_gc_cycles
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
