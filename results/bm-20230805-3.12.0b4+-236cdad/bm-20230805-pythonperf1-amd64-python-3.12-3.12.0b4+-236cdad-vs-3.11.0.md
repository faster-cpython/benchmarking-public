
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: 236cdad
- commit date: 2023-08-05
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4+-236cdad |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 214 ms: 1.03x slower                                        |
| docutils       | 1.60 sec                                                    | 1.66 sec: 1.04x slower                                      |
| tornado_http   | 91.8 ms                                                     | 89.3 ms: 1.03x faster                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4+-236cdad |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 148 ms: 1.00x faster                                        |
| Geometric mean | (ref)                                                       | 1.00x faster                                                |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4+-236cdad |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 86.9 ms: 1.04x faster                                       |
| regex_v8       | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                       |
| regex_dna      | 115 ms                                                      | 124 ms: 1.08x slower                                        |
| regex_effbot   | 1.50 ms                                                     | 1.64 ms: 1.10x slower                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4+-236cdad |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.76 ms: 1.31x faster                                       |
| unpickle_pure_python | 152 us                                                      | 135 us: 1.12x faster                                        |
| xml_etree_parse      | 95.9 ms                                                     | 90.6 ms: 1.06x faster                                       |
| tomli_loads          | 1.41 sec                                                    | 1.37 sec: 1.03x faster                                      |
| pickle_pure_python   | 200 us                                                      | 197 us: 1.02x faster                                        |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.5 ms: 1.02x slower                                       |
| xml_etree_process    | 37.1 ms                                                     | 38.5 ms: 1.04x slower                                       |
| unpickle             | 8.09 us                                                     | 8.48 us: 1.05x slower                                       |
| json_loads           | 12.9 us                                                     | 13.6 us: 1.06x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.88 us: 1.07x slower                                       |
| xml_etree_generate   | 52.2 ms                                                     | 56.6 ms: 1.08x slower                                       |
| pickle               | 6.61 us                                                     | 7.24 us: 1.10x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.84 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4+-236cdad |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4+-236cdad |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.20 ms: 1.01x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4+-236cdad |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 100.0 us: 3.22x faster                                      |
| generators               | 33.8 ms                                                     | 22.7 ms: 1.49x faster                                       |
| asyncio_tcp              | 699 ms                                                      | 491 ms: 1.42x faster                                        |
| json_dumps               | 7.56 ms                                                     | 5.76 ms: 1.31x faster                                       |
| richards_super           | 37.5 ms                                                     | 29.4 ms: 1.27x faster                                       |
| deltablue                | 2.61 ms                                                     | 2.20 ms: 1.19x faster                                       |
| unpack_sequence          | 46.1 ns                                                     | 39.0 ns: 1.18x faster                                       |
| richards                 | 30.6 ms                                                     | 26.1 ms: 1.17x faster                                       |
| sqlglot_parse            | 952 us                                                      | 823 us: 1.16x faster                                        |
| logging_silent           | 69.8 ns                                                     | 60.8 ns: 1.15x faster                                       |
| mdp                      | 1.67 sec                                                    | 1.46 sec: 1.14x faster                                      |
| unpickle_pure_python     | 152 us                                                      | 135 us: 1.12x faster                                        |
| comprehensions           | 15.9 us                                                     | 14.2 us: 1.12x faster                                       |
| go                       | 97.3 ms                                                     | 86.9 ms: 1.12x faster                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 1.04 ms: 1.12x faster                                       |
| hexiom                   | 4.55 ms                                                     | 4.12 ms: 1.11x faster                                       |
| raytrace                 | 211 ms                                                      | 191 ms: 1.11x faster                                        |
| chaos                    | 47.1 ms                                                     | 42.9 ms: 1.10x faster                                       |
| json                     | 3.25 ms                                                     | 2.97 ms: 1.10x faster                                       |
| coverage                 | 55.9 ms                                                     | 51.2 ms: 1.09x faster                                       |
| scimark_lu               | 63.5 ms                                                     | 58.5 ms: 1.09x faster                                       |
| fannkuch                 | 252 ms                                                      | 234 ms: 1.08x faster                                        |
| async_tree_none          | 320 ms                                                      | 298 ms: 1.07x faster                                        |
| mypy2                    | 229 ms                                                      | 213 ms: 1.07x faster                                        |
| async_tree_memoization   | 371 ms                                                      | 348 ms: 1.06x faster                                        |
| deepcopy_memo            | 25.2 us                                                     | 23.7 us: 1.06x faster                                       |
| xml_etree_parse          | 95.9 ms                                                     | 90.6 ms: 1.06x faster                                       |
| spectral_norm            | 67.9 ms                                                     | 64.2 ms: 1.06x faster                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.00 sec: 1.05x faster                                      |
| nqueens                  | 64.9 ms                                                     | 61.6 ms: 1.05x faster                                       |
| deepcopy                 | 246 us                                                      | 233 us: 1.05x faster                                        |
| async_tree_io            | 779 ms                                                      | 744 ms: 1.05x faster                                        |
| regex_compile            | 90.6 ms                                                     | 86.9 ms: 1.04x faster                                       |
| scimark_monte_carlo      | 44.6 ms                                                     | 43.2 ms: 1.03x faster                                       |
| tomli_loads              | 1.41 sec                                                    | 1.37 sec: 1.03x faster                                      |
| tornado_http             | 91.8 ms                                                     | 89.3 ms: 1.03x faster                                       |
| coroutines               | 14.6 ms                                                     | 14.2 ms: 1.03x faster                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 488 ms: 1.03x faster                                        |
| logging_simple           | 6.61 us                                                     | 6.46 us: 1.02x faster                                       |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.52 ms: 1.02x faster                                       |
| meteor_contest           | 74.7 ms                                                     | 73.5 ms: 1.02x faster                                       |
| pickle_pure_python       | 200 us                                                      | 197 us: 1.02x faster                                        |
| aiohttp                  | 899 us                                                      | 886 us: 1.02x faster                                        |
| sqlglot_normalize        | 190 ms                                                      | 188 ms: 1.01x faster                                        |
| pyflate                  | 304 ms                                                      | 301 ms: 1.01x faster                                        |
| mako                     | 7.26 ms                                                     | 7.20 ms: 1.01x faster                                       |
| dulwich_log              | 44.5 ms                                                     | 44.2 ms: 1.01x faster                                       |
| pidigits                 | 148 ms                                                      | 148 ms: 1.00x faster                                        |
| scimark_fft              | 178 ms                                                      | 180 ms: 1.01x slower                                        |
| deepcopy_reduce          | 2.07 us                                                     | 2.09 us: 1.01x slower                                       |
| python_startup           | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                       |
| regex_v8                 | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                       |
| xml_etree_iterparse      | 62.6 ms                                                     | 63.5 ms: 1.02x slower                                       |
| 2to3                     | 209 ms                                                      | 214 ms: 1.03x slower                                        |
| crypto_pyaes             | 47.6 ms                                                     | 48.9 ms: 1.03x slower                                       |
| sqlite_synth             | 1.68 us                                                     | 1.73 us: 1.03x slower                                       |
| docutils                 | 1.60 sec                                                    | 1.66 sec: 1.04x slower                                      |
| scimark_sor              | 75.6 ms                                                     | 78.4 ms: 1.04x slower                                       |
| xml_etree_process        | 37.1 ms                                                     | 38.5 ms: 1.04x slower                                       |
| unpickle                 | 8.09 us                                                     | 8.48 us: 1.05x slower                                       |
| telco                    | 3.90 ms                                                     | 4.10 ms: 1.05x slower                                       |
| gc_traversal             | 1.46 ms                                                     | 1.53 ms: 1.05x slower                                       |
| json_loads               | 12.9 us                                                     | 13.6 us: 1.06x slower                                       |
| pickle_list              | 2.68 us                                                     | 2.88 us: 1.07x slower                                       |
| regex_dna                | 115 ms                                                      | 124 ms: 1.08x slower                                        |
| create_gc_cycles         | 693 us                                                      | 747 us: 1.08x slower                                        |
| bench_mp_pool            | 62.5 ms                                                     | 67.6 ms: 1.08x slower                                       |
| xml_etree_generate       | 52.2 ms                                                     | 56.6 ms: 1.08x slower                                       |
| regex_effbot             | 1.50 ms                                                     | 1.64 ms: 1.10x slower                                       |
| pickle                   | 6.61 us                                                     | 7.24 us: 1.10x slower                                       |
| unpickle_list            | 2.55 us                                                     | 2.84 us: 1.11x slower                                       |
| pathlib                  | 71.4 ms                                                     | 83.9 ms: 1.18x slower                                       |
| async_generators         | 178 ms                                                      | 235 ms: 1.33x slower                                        |
| dask                     | 264 ms                                                      | 366 ms: 1.39x slower                                        |
| Geometric mean           | (ref)                                                       | 1.04x faster                                                |

Benchmark hidden because not significant (10): logging_format, pickle_dict, pprint_pformat, nbody, pycparser, float, sqlglot_optimize, python_startup_no_site, pprint_safe_repr, bench_thread_pool
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
