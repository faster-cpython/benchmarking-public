
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 6996b40
- commit date: 2023-08-05
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.73 sec: 1.08x slower                                     |
| tornado_http   | 91.8 ms                                                     | 90.0 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                       |
| float          | 54.6 ms                                                     | 59.2 ms: 1.08x slower                                      |
| nbody          | 70.0 ms                                                     | 83.0 ms: 1.19x slower                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                       |
| regex_compile  | 90.6 ms                                                     | 96.8 ms: 1.07x slower                                      |
| regex_effbot   | 1.50 ms                                                     | 1.63 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40 |
|---------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps          | 7.56 ms                                                     | 5.83 ms: 1.30x faster                                      |
| pickle_pure_python  | 200 us                                                      | 205 us: 1.02x slower                                       |
| unpickle            | 8.09 us                                                     | 8.32 us: 1.03x slower                                      |
| xml_etree_parse     | 95.9 ms                                                     | 99.1 ms: 1.03x slower                                      |
| pickle_list         | 2.68 us                                                     | 2.80 us: 1.05x slower                                      |
| xml_etree_iterparse | 62.6 ms                                                     | 66.6 ms: 1.07x slower                                      |
| pickle              | 6.61 us                                                     | 7.07 us: 1.07x slower                                      |
| json_loads          | 12.9 us                                                     | 13.9 us: 1.08x slower                                      |
| xml_etree_process   | 37.1 ms                                                     | 40.4 ms: 1.09x slower                                      |
| xml_etree_generate  | 52.2 ms                                                     | 57.8 ms: 1.11x slower                                      |
| unpickle_list       | 2.55 us                                                     | 2.83 us: 1.11x slower                                      |
| tomli_loads         | 1.41 sec                                                    | 1.66 sec: 1.18x slower                                     |
| Geometric mean      | (ref)                                                       | 1.04x slower                                               |

Benchmark hidden because not significant (2): pickle_dict, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.4 ms: 1.03x slower                                      |
| python_startup         | 18.7 ms                                                     | 19.4 ms: 1.04x slower                                      |
| Geometric mean         | (ref)                                                       | 1.04x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40 |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.92 ms: 1.09x slower                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 103 us: 3.14x faster                                       |
| asyncio_tcp              | 699 ms                                                      | 508 ms: 1.38x faster                                       |
| json_dumps               | 7.56 ms                                                     | 5.83 ms: 1.30x faster                                      |
| generators               | 33.8 ms                                                     | 27.0 ms: 1.25x faster                                      |
| unpack_sequence          | 46.1 ns                                                     | 39.2 ns: 1.18x faster                                      |
| json                     | 3.25 ms                                                     | 2.92 ms: 1.11x faster                                      |
| raytrace                 | 211 ms                                                      | 193 ms: 1.09x faster                                       |
| richards_super           | 37.5 ms                                                     | 34.5 ms: 1.09x faster                                      |
| deltablue                | 2.61 ms                                                     | 2.44 ms: 1.07x faster                                      |
| sqlglot_parse            | 952 us                                                      | 901 us: 1.06x faster                                       |
| chaos                    | 47.1 ms                                                     | 44.8 ms: 1.05x faster                                      |
| mdp                      | 1.67 sec                                                    | 1.60 sec: 1.04x faster                                     |
| sqlglot_transpile        | 1.16 ms                                                     | 1.11 ms: 1.04x faster                                      |
| comprehensions           | 15.9 us                                                     | 15.4 us: 1.03x faster                                      |
| async_tree_none          | 320 ms                                                      | 313 ms: 1.02x faster                                       |
| logging_silent           | 69.8 ns                                                     | 68.2 ns: 1.02x faster                                      |
| async_tree_memoization   | 371 ms                                                      | 364 ms: 1.02x faster                                       |
| tornado_http             | 91.8 ms                                                     | 90.0 ms: 1.02x faster                                      |
| mypy2                    | 229 ms                                                      | 225 ms: 1.02x faster                                       |
| coverage                 | 55.9 ms                                                     | 55.1 ms: 1.01x faster                                      |
| crypto_pyaes             | 47.6 ms                                                     | 47.1 ms: 1.01x faster                                      |
| scimark_lu               | 63.5 ms                                                     | 63.1 ms: 1.01x faster                                      |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                       |
| fannkuch                 | 252 ms                                                      | 256 ms: 1.01x slower                                       |
| richards                 | 30.6 ms                                                     | 31.0 ms: 1.01x slower                                      |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.62 ms: 1.02x slower                                      |
| pickle_pure_python       | 200 us                                                      | 205 us: 1.02x slower                                       |
| unpickle                 | 8.09 us                                                     | 8.32 us: 1.03x slower                                      |
| meteor_contest           | 74.7 ms                                                     | 76.9 ms: 1.03x slower                                      |
| sqlglot_optimize         | 34.9 ms                                                     | 36.0 ms: 1.03x slower                                      |
| xml_etree_parse          | 95.9 ms                                                     | 99.1 ms: 1.03x slower                                      |
| hexiom                   | 4.55 ms                                                     | 4.70 ms: 1.03x slower                                      |
| python_startup_no_site   | 15.9 ms                                                     | 16.4 ms: 1.03x slower                                      |
| deepcopy                 | 246 us                                                      | 254 us: 1.04x slower                                       |
| bench_thread_pool        | 852 us                                                      | 883 us: 1.04x slower                                       |
| deepcopy_memo            | 25.2 us                                                     | 26.1 us: 1.04x slower                                      |
| python_startup           | 18.7 ms                                                     | 19.4 ms: 1.04x slower                                      |
| sqlglot_normalize        | 190 ms                                                      | 198 ms: 1.04x slower                                       |
| spectral_norm            | 67.9 ms                                                     | 71.0 ms: 1.05x slower                                      |
| pickle_list              | 2.68 us                                                     | 2.80 us: 1.05x slower                                      |
| pprint_pformat           | 1.04 sec                                                    | 1.09 sec: 1.05x slower                                     |
| gc_traversal             | 1.46 ms                                                     | 1.54 ms: 1.05x slower                                      |
| go                       | 97.3 ms                                                     | 103 ms: 1.05x slower                                       |
| scimark_monte_carlo      | 44.6 ms                                                     | 47.2 ms: 1.06x slower                                      |
| regex_dna                | 115 ms                                                      | 122 ms: 1.06x slower                                       |
| pprint_safe_repr         | 512 ms                                                      | 542 ms: 1.06x slower                                       |
| pyflate                  | 304 ms                                                      | 324 ms: 1.06x slower                                       |
| xml_etree_iterparse      | 62.6 ms                                                     | 66.6 ms: 1.07x slower                                      |
| logging_simple           | 6.61 us                                                     | 7.05 us: 1.07x slower                                      |
| regex_compile            | 90.6 ms                                                     | 96.8 ms: 1.07x slower                                      |
| sqlite_synth             | 1.68 us                                                     | 1.80 us: 1.07x slower                                      |
| pickle                   | 6.61 us                                                     | 7.07 us: 1.07x slower                                      |
| scimark_fft              | 178 ms                                                      | 192 ms: 1.07x slower                                       |
| json_loads               | 12.9 us                                                     | 13.9 us: 1.08x slower                                      |
| docutils                 | 1.60 sec                                                    | 1.73 sec: 1.08x slower                                     |
| dulwich_log              | 44.5 ms                                                     | 48.1 ms: 1.08x slower                                      |
| bench_mp_pool            | 62.5 ms                                                     | 67.7 ms: 1.08x slower                                      |
| float                    | 54.6 ms                                                     | 59.2 ms: 1.08x slower                                      |
| create_gc_cycles         | 693 us                                                      | 752 us: 1.09x slower                                       |
| coroutines               | 14.6 ms                                                     | 15.9 ms: 1.09x slower                                      |
| xml_etree_process        | 37.1 ms                                                     | 40.4 ms: 1.09x slower                                      |
| mako                     | 7.26 ms                                                     | 7.92 ms: 1.09x slower                                      |
| regex_effbot             | 1.50 ms                                                     | 1.63 ms: 1.09x slower                                      |
| pycparser                | 691 ms                                                      | 755 ms: 1.09x slower                                       |
| deepcopy_reduce          | 2.07 us                                                     | 2.28 us: 1.10x slower                                      |
| logging_format           | 7.01 us                                                     | 7.75 us: 1.11x slower                                      |
| xml_etree_generate       | 52.2 ms                                                     | 57.8 ms: 1.11x slower                                      |
| unpickle_list            | 2.55 us                                                     | 2.83 us: 1.11x slower                                      |
| scimark_sor              | 75.6 ms                                                     | 87.2 ms: 1.15x slower                                      |
| tomli_loads              | 1.41 sec                                                    | 1.66 sec: 1.18x slower                                     |
| pathlib                  | 71.4 ms                                                     | 84.3 ms: 1.18x slower                                      |
| nbody                    | 70.0 ms                                                     | 83.0 ms: 1.19x slower                                      |
| telco                    | 3.90 ms                                                     | 5.16 ms: 1.32x slower                                      |
| async_generators         | 178 ms                                                      | 250 ms: 1.41x slower                                       |
| dask                     | 264 ms                                                      | 389 ms: 1.47x slower                                       |
| Geometric mean           | (ref)                                                       | 1.02x slower                                               |

Benchmark hidden because not significant (7): asyncio_tcp_ssl, pickle_dict, unpickle_pure_python, async_tree_io, nqueens, async_tree_cpu_io_mixed, regex_v8
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
