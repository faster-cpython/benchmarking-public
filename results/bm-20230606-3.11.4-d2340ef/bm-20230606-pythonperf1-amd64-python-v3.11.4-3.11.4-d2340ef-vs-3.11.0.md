
# Results vs. 3.11.0

- fork: python
- ref: v3.11.4
- machine: windows-amd64
- commit hash: d2340ef
- commit date: 2023-06-06
- overall geometric mean: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf1-amd64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 221 ms: 1.06x slower                                        |
| chameleon      | 5.11 ms                                                     | 5.44 ms: 1.06x slower                                       |
| docutils       | 1.60 sec                                                    | 1.66 sec: 1.04x slower                                      |
| html5lib       | 37.5 ms                                                     | 39.4 ms: 1.05x slower                                       |
| tornado_http   | 91.8 ms                                                     | 103 ms: 1.13x slower                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf1-amd64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                        |
| float          | 54.6 ms                                                     | 56.7 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf1-amd64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 1.50 ms                                                     | 1.52 ms: 1.01x slower                                       |
| regex_compile  | 90.6 ms                                                     | 92.8 ms: 1.02x slower                                       |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                       | 1.02x slower                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf1-amd64-python-v3.11.4-3.11.4-d2340ef |
|---------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_pure_python  | 200 us                                                      | 201 us: 1.01x slower                                        |
| unpickle            | 8.09 us                                                     | 8.15 us: 1.01x slower                                       |
| tomli_loads         | 1.41 sec                                                    | 1.43 sec: 1.01x slower                                      |
| pickle              | 6.61 us                                                     | 6.74 us: 1.02x slower                                       |
| xml_etree_process   | 37.1 ms                                                     | 37.9 ms: 1.02x slower                                       |
| json_loads          | 12.9 us                                                     | 13.3 us: 1.03x slower                                       |
| xml_etree_generate  | 52.2 ms                                                     | 53.8 ms: 1.03x slower                                       |
| xml_etree_iterparse | 62.6 ms                                                     | 64.8 ms: 1.04x slower                                       |
| pickle_list         | 2.68 us                                                     | 2.78 us: 1.04x slower                                       |
| json_dumps          | 7.56 ms                                                     | 7.92 ms: 1.05x slower                                       |
| unpickle_list       | 2.55 us                                                     | 2.73 us: 1.07x slower                                       |
| Geometric mean      | (ref)                                                       | 1.02x slower                                                |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_pure_python, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf1-amd64-python-v3.11.4-3.11.4-d2340ef |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 17.5 ms: 1.10x slower                                       |
| python_startup         | 18.7 ms                                                     | 20.6 ms: 1.10x slower                                       |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf1-amd64-python-v3.11.4-3.11.4-d2340ef |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 24.1 ms                                                     | 24.5 ms: 1.01x slower                                       |
| genshi_xml      | 37.3 ms                                                     | 38.6 ms: 1.03x slower                                       |
| genshi_text     | 17.0 ms                                                     | 17.8 ms: 1.05x slower                                       |
| mako            | 7.26 ms                                                     | 7.67 ms: 1.06x slower                                       |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf1-amd64-python-v3.11.4-3.11.4-d2340ef |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| comprehensions           | 15.9 us                                                     | 15.6 us: 1.02x faster                                       |
| sqlglot_parse            | 952 us                                                      | 936 us: 1.02x faster                                        |
| raytrace                 | 211 ms                                                      | 208 ms: 1.02x faster                                        |
| sqlglot_transpile        | 1.16 ms                                                     | 1.15 ms: 1.01x faster                                       |
| thrift                   | 491 us                                                      | 486 us: 1.01x faster                                        |
| coverage                 | 55.9 ms                                                     | 55.6 ms: 1.00x faster                                       |
| pickle_pure_python       | 200 us                                                      | 201 us: 1.01x slower                                        |
| unpickle                 | 8.09 us                                                     | 8.15 us: 1.01x slower                                       |
| sympy_integrate          | 13.8 ms                                                     | 13.9 ms: 1.01x slower                                       |
| deepcopy_reduce          | 2.07 us                                                     | 2.09 us: 1.01x slower                                       |
| scimark_monte_carlo      | 44.6 ms                                                     | 45.1 ms: 1.01x slower                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 35.2 ms: 1.01x slower                                       |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.60 ms: 1.01x slower                                       |
| sqlglot_normalize        | 190 ms                                                      | 193 ms: 1.01x slower                                        |
| pprint_pformat           | 1.04 sec                                                    | 1.05 sec: 1.01x slower                                      |
| regex_effbot             | 1.50 ms                                                     | 1.52 ms: 1.01x slower                                       |
| tomli_loads              | 1.41 sec                                                    | 1.43 sec: 1.01x slower                                      |
| typing_runtime_protocols | 322 us                                                      | 326 us: 1.01x slower                                        |
| coroutines               | 14.6 ms                                                     | 14.8 ms: 1.01x slower                                       |
| richards                 | 30.6 ms                                                     | 31.0 ms: 1.01x slower                                       |
| sympy_expand             | 295 ms                                                      | 299 ms: 1.01x slower                                        |
| logging_simple           | 6.61 us                                                     | 6.71 us: 1.01x slower                                       |
| django_template          | 24.1 ms                                                     | 24.5 ms: 1.01x slower                                       |
| sqlalchemy_declarative   | 81.5 ms                                                     | 82.7 ms: 1.02x slower                                       |
| deepcopy_memo            | 25.2 us                                                     | 25.6 us: 1.02x slower                                       |
| scimark_sor              | 75.6 ms                                                     | 76.9 ms: 1.02x slower                                       |
| pidigits                 | 148 ms                                                      | 151 ms: 1.02x slower                                        |
| pyflate                  | 304 ms                                                      | 310 ms: 1.02x slower                                        |
| pickle                   | 6.61 us                                                     | 6.74 us: 1.02x slower                                       |
| generators               | 33.8 ms                                                     | 34.5 ms: 1.02x slower                                       |
| sqlalchemy_imperative    | 10.2 ms                                                     | 10.4 ms: 1.02x slower                                       |
| xml_etree_process        | 37.1 ms                                                     | 37.9 ms: 1.02x slower                                       |
| regex_compile            | 90.6 ms                                                     | 92.8 ms: 1.02x slower                                       |
| telco                    | 3.90 ms                                                     | 4.00 ms: 1.03x slower                                       |
| sympy_str                | 182 ms                                                      | 187 ms: 1.03x slower                                        |
| json_loads               | 12.9 us                                                     | 13.3 us: 1.03x slower                                       |
| scimark_fft              | 178 ms                                                      | 184 ms: 1.03x slower                                        |
| sympy_sum                | 99.9 ms                                                     | 103 ms: 1.03x slower                                        |
| richards_super           | 37.5 ms                                                     | 38.6 ms: 1.03x slower                                       |
| xml_etree_generate       | 52.2 ms                                                     | 53.8 ms: 1.03x slower                                       |
| go                       | 97.3 ms                                                     | 100 ms: 1.03x slower                                        |
| logging_silent           | 69.8 ns                                                     | 72.1 ns: 1.03x slower                                       |
| genshi_xml               | 37.3 ms                                                     | 38.6 ms: 1.03x slower                                       |
| logging_format           | 7.01 us                                                     | 7.26 us: 1.03x slower                                       |
| meteor_contest           | 74.7 ms                                                     | 77.4 ms: 1.04x slower                                       |
| chaos                    | 47.1 ms                                                     | 48.8 ms: 1.04x slower                                       |
| xml_etree_iterparse      | 62.6 ms                                                     | 64.8 ms: 1.04x slower                                       |
| docutils                 | 1.60 sec                                                    | 1.66 sec: 1.04x slower                                      |
| float                    | 54.6 ms                                                     | 56.7 ms: 1.04x slower                                       |
| pickle_list              | 2.68 us                                                     | 2.78 us: 1.04x slower                                       |
| deltablue                | 2.61 ms                                                     | 2.71 ms: 1.04x slower                                       |
| async_generators         | 178 ms                                                      | 184 ms: 1.04x slower                                        |
| regex_dna                | 115 ms                                                      | 120 ms: 1.04x slower                                        |
| gc_traversal             | 1.46 ms                                                     | 1.52 ms: 1.04x slower                                       |
| aiohttp                  | 899 us                                                      | 936 us: 1.04x slower                                        |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 522 ms: 1.04x slower                                        |
| dulwich_log              | 44.5 ms                                                     | 46.4 ms: 1.04x slower                                       |
| async_tree_io            | 779 ms                                                      | 813 ms: 1.04x slower                                        |
| async_tree_none          | 320 ms                                                      | 334 ms: 1.04x slower                                        |
| crypto_pyaes             | 47.6 ms                                                     | 49.7 ms: 1.04x slower                                       |
| fannkuch                 | 252 ms                                                      | 263 ms: 1.04x slower                                        |
| unpack_sequence          | 46.1 ns                                                     | 48.1 ns: 1.04x slower                                       |
| sqlite_synth             | 1.68 us                                                     | 1.76 us: 1.05x slower                                       |
| genshi_text              | 17.0 ms                                                     | 17.8 ms: 1.05x slower                                       |
| json_dumps               | 7.56 ms                                                     | 7.92 ms: 1.05x slower                                       |
| html5lib                 | 37.5 ms                                                     | 39.4 ms: 1.05x slower                                       |
| pycparser                | 691 ms                                                      | 726 ms: 1.05x slower                                        |
| mdp                      | 1.67 sec                                                    | 1.76 sec: 1.05x slower                                      |
| mako                     | 7.26 ms                                                     | 7.67 ms: 1.06x slower                                       |
| bench_mp_pool            | 62.5 ms                                                     | 66.1 ms: 1.06x slower                                       |
| async_tree_memoization   | 371 ms                                                      | 392 ms: 1.06x slower                                        |
| 2to3                     | 209 ms                                                      | 221 ms: 1.06x slower                                        |
| chameleon                | 5.11 ms                                                     | 5.44 ms: 1.06x slower                                       |
| create_gc_cycles         | 693 us                                                      | 740 us: 1.07x slower                                        |
| unpickle_list            | 2.55 us                                                     | 2.73 us: 1.07x slower                                       |
| dask                     | 264 ms                                                      | 287 ms: 1.08x slower                                        |
| pathlib                  | 71.4 ms                                                     | 77.5 ms: 1.09x slower                                       |
| spectral_norm            | 67.9 ms                                                     | 74.7 ms: 1.10x slower                                       |
| python_startup_no_site   | 15.9 ms                                                     | 17.5 ms: 1.10x slower                                       |
| bench_thread_pool        | 852 us                                                      | 941 us: 1.10x slower                                        |
| python_startup           | 18.7 ms                                                     | 20.6 ms: 1.10x slower                                       |
| tornado_http             | 91.8 ms                                                     | 103 ms: 1.13x slower                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.41 sec: 1.14x slower                                      |
| mypy2                    | 229 ms                                                      | 290 ms: 1.27x slower                                        |
| asyncio_tcp              | 699 ms                                                      | 932 ms: 1.33x slower                                        |
| Geometric mean           | (ref)                                                       | 1.04x slower                                                |

Benchmark hidden because not significant (13): scimark_lu, hexiom, deepcopy, flaskblogging, nqueens, pprint_safe_repr, xml_etree_parse, regex_v8, unpickle_pure_python, nbody, pickle_dict, pylint, json
