
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: d87d67b
- commit date: 2023-07-23
- overall geometric mean: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| tornado_http   | 91.8 ms                                                     | 87.1 ms: 1.05x faster                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 54.6 ms                                                     | 52.1 ms: 1.05x faster                                       |
| nbody          | 70.0 ms                                                     | 66.9 ms: 1.05x faster                                       |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                       | 1.03x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 85.7 ms: 1.06x faster                                       |
| regex_v8       | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                       |
| regex_dna      | 115 ms                                                      | 123 ms: 1.07x slower                                        |
| regex_effbot   | 1.50 ms                                                     | 1.62 ms: 1.08x slower                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4+-d87d67b |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.67 ms: 1.33x faster                                       |
| unpickle_pure_python | 152 us                                                      | 129 us: 1.18x faster                                        |
| pickle_pure_python   | 200 us                                                      | 189 us: 1.06x faster                                        |
| tomli_loads          | 1.41 sec                                                    | 1.34 sec: 1.06x faster                                      |
| xml_etree_parse      | 95.9 ms                                                     | 91.3 ms: 1.05x faster                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                       |
| unpickle             | 8.09 us                                                     | 8.34 us: 1.03x slower                                       |
| xml_etree_generate   | 52.2 ms                                                     | 54.5 ms: 1.04x slower                                       |
| json_loads           | 12.9 us                                                     | 13.6 us: 1.05x slower                                       |
| pickle               | 6.61 us                                                     | 7.12 us: 1.08x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.90 us: 1.08x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.78 us: 1.09x slower                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                |

Benchmark hidden because not significant (2): xml_etree_process, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4+-d87d67b |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.6 ms: 1.02x faster                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4+-d87d67b |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.77 ms: 1.07x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4+-d87d67b |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 92.0 us: 3.50x faster                                       |
| generators               | 33.8 ms                                                     | 21.5 ms: 1.58x faster                                       |
| asyncio_tcp              | 699 ms                                                      | 470 ms: 1.49x faster                                        |
| json_dumps               | 7.56 ms                                                     | 5.67 ms: 1.33x faster                                       |
| richards_super           | 37.5 ms                                                     | 29.4 ms: 1.28x faster                                       |
| deltablue                | 2.61 ms                                                     | 2.06 ms: 1.27x faster                                       |
| mdp                      | 1.67 sec                                                    | 1.34 sec: 1.25x faster                                      |
| sqlglot_parse            | 952 us                                                      | 785 us: 1.21x faster                                        |
| logging_silent           | 69.8 ns                                                     | 58.1 ns: 1.20x faster                                       |
| richards                 | 30.6 ms                                                     | 26.0 ms: 1.18x faster                                       |
| unpickle_pure_python     | 152 us                                                      | 129 us: 1.18x faster                                        |
| sqlglot_transpile        | 1.16 ms                                                     | 996 us: 1.17x faster                                        |
| hexiom                   | 4.55 ms                                                     | 3.90 ms: 1.17x faster                                       |
| unpack_sequence          | 46.1 ns                                                     | 39.7 ns: 1.16x faster                                       |
| raytrace                 | 211 ms                                                      | 182 ms: 1.16x faster                                        |
| comprehensions           | 15.9 us                                                     | 13.8 us: 1.15x faster                                       |
| go                       | 97.3 ms                                                     | 85.9 ms: 1.13x faster                                       |
| scimark_lu               | 63.5 ms                                                     | 56.5 ms: 1.12x faster                                       |
| async_tree_none          | 320 ms                                                      | 285 ms: 1.12x faster                                        |
| async_tree_memoization   | 371 ms                                                      | 331 ms: 1.12x faster                                        |
| async_tree_io            | 779 ms                                                      | 697 ms: 1.12x faster                                        |
| coverage                 | 55.9 ms                                                     | 50.3 ms: 1.11x faster                                       |
| json                     | 3.25 ms                                                     | 2.93 ms: 1.11x faster                                       |
| chaos                    | 47.1 ms                                                     | 42.6 ms: 1.11x faster                                       |
| spectral_norm            | 67.9 ms                                                     | 61.6 ms: 1.10x faster                                       |
| mypy2                    | 229 ms                                                      | 209 ms: 1.10x faster                                        |
| deepcopy                 | 246 us                                                      | 228 us: 1.08x faster                                        |
| deepcopy_memo            | 25.2 us                                                     | 23.4 us: 1.08x faster                                       |
| mako                     | 7.26 ms                                                     | 6.77 ms: 1.07x faster                                       |
| sqlglot_normalize        | 190 ms                                                      | 177 ms: 1.07x faster                                        |
| nqueens                  | 64.9 ms                                                     | 60.6 ms: 1.07x faster                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 469 ms: 1.07x faster                                        |
| scimark_monte_carlo      | 44.6 ms                                                     | 41.8 ms: 1.07x faster                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.98 sec: 1.07x faster                                      |
| pickle_pure_python       | 200 us                                                      | 189 us: 1.06x faster                                        |
| aiohttp                  | 899 us                                                      | 850 us: 1.06x faster                                        |
| regex_compile            | 90.6 ms                                                     | 85.7 ms: 1.06x faster                                       |
| tomli_loads              | 1.41 sec                                                    | 1.34 sec: 1.06x faster                                      |
| tornado_http             | 91.8 ms                                                     | 87.1 ms: 1.05x faster                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 33.1 ms: 1.05x faster                                       |
| pyflate                  | 304 ms                                                      | 289 ms: 1.05x faster                                        |
| fannkuch                 | 252 ms                                                      | 240 ms: 1.05x faster                                        |
| xml_etree_parse          | 95.9 ms                                                     | 91.3 ms: 1.05x faster                                       |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.45 ms: 1.05x faster                                       |
| float                    | 54.6 ms                                                     | 52.1 ms: 1.05x faster                                       |
| coroutines               | 14.6 ms                                                     | 14.0 ms: 1.05x faster                                       |
| nbody                    | 70.0 ms                                                     | 66.9 ms: 1.05x faster                                       |
| logging_simple           | 6.61 us                                                     | 6.35 us: 1.04x faster                                       |
| pycparser                | 691 ms                                                      | 665 ms: 1.04x faster                                        |
| bench_thread_pool        | 852 us                                                      | 821 us: 1.04x faster                                        |
| scimark_fft              | 178 ms                                                      | 172 ms: 1.03x faster                                        |
| dulwich_log              | 44.5 ms                                                     | 43.1 ms: 1.03x faster                                       |
| logging_format           | 7.01 us                                                     | 6.83 us: 1.03x faster                                       |
| crypto_pyaes             | 47.6 ms                                                     | 46.4 ms: 1.02x faster                                       |
| python_startup_no_site   | 15.9 ms                                                     | 15.6 ms: 1.02x faster                                       |
| meteor_contest           | 74.7 ms                                                     | 73.4 ms: 1.02x faster                                       |
| deepcopy_reduce          | 2.07 us                                                     | 2.04 us: 1.02x faster                                       |
| pprint_pformat           | 1.04 sec                                                    | 1.03 sec: 1.01x faster                                      |
| pprint_safe_repr         | 512 ms                                                      | 508 ms: 1.01x faster                                        |
| gc_traversal             | 1.46 ms                                                     | 1.47 ms: 1.01x slower                                       |
| xml_etree_iterparse      | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                       |
| regex_v8                 | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                       |
| pidigits                 | 148 ms                                                      | 151 ms: 1.02x slower                                        |
| unpickle                 | 8.09 us                                                     | 8.34 us: 1.03x slower                                       |
| sqlite_synth             | 1.68 us                                                     | 1.74 us: 1.03x slower                                       |
| telco                    | 3.90 ms                                                     | 4.05 ms: 1.04x slower                                       |
| scimark_sor              | 75.6 ms                                                     | 78.5 ms: 1.04x slower                                       |
| create_gc_cycles         | 693 us                                                      | 721 us: 1.04x slower                                        |
| xml_etree_generate       | 52.2 ms                                                     | 54.5 ms: 1.04x slower                                       |
| json_loads               | 12.9 us                                                     | 13.6 us: 1.05x slower                                       |
| regex_dna                | 115 ms                                                      | 123 ms: 1.07x slower                                        |
| bench_mp_pool            | 62.5 ms                                                     | 67.2 ms: 1.07x slower                                       |
| pickle                   | 6.61 us                                                     | 7.12 us: 1.08x slower                                       |
| pickle_list              | 2.68 us                                                     | 2.90 us: 1.08x slower                                       |
| regex_effbot             | 1.50 ms                                                     | 1.62 ms: 1.08x slower                                       |
| unpickle_list            | 2.55 us                                                     | 2.78 us: 1.09x slower                                       |
| pathlib                  | 71.4 ms                                                     | 78.9 ms: 1.11x slower                                       |
| async_generators         | 178 ms                                                      | 225 ms: 1.27x slower                                        |
| dask                     | 264 ms                                                      | 358 ms: 1.35x slower                                        |
| Geometric mean           | (ref)                                                       | 1.07x faster                                                |

Benchmark hidden because not significant (5): python_startup, xml_etree_process, 2to3, docutils, pickle_dict
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
