
# Results vs. 3.11.0

- fork: python
- ref: f3909b8bc83675b7ab09
- machine: windows-amd64
- commit hash: f3909b8
- commit date: 2023-04-04
- overall geometric mean: 1.00x slower \*
- HPT reliability: 90.24%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf1-amd64-python-f3909b8bc83675b7ab09-3.11.3-f3909b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 206 ms: 1.01x faster                                                     |
| chameleon      | 5.11 ms                                                     | 5.27 ms: 1.03x slower                                                    |
| docutils       | 1.60 sec                                                    | 1.58 sec: 1.01x faster                                                   |
| html5lib       | 37.5 ms                                                     | 39.8 ms: 1.06x slower                                                    |
| tornado_http   | 91.8 ms                                                     | 90.1 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                       | 1.01x slower                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf1-amd64-python-f3909b8bc83675b7ab09-3.11.3-f3909b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 52.6 ms: 1.04x faster                                                    |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                       | 1.02x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf1-amd64-python-f3909b8bc83675b7ab09-3.11.3-f3909b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 89.7 ms: 1.01x faster                                                    |
| regex_v8       | 13.8 ms                                                     | 14.3 ms: 1.03x slower                                                    |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                     |
| regex_effbot   | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                       | 1.03x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf1-amd64-python-f3909b8bc83675b7ab09-3.11.3-f3909b8 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 95.9 ms                                                     | 91.3 ms: 1.05x faster                                                    |
| xml_etree_process    | 37.1 ms                                                     | 36.3 ms: 1.02x faster                                                    |
| xml_etree_iterparse  | 62.6 ms                                                     | 61.4 ms: 1.02x faster                                                    |
| unpickle             | 8.09 us                                                     | 7.97 us: 1.02x faster                                                    |
| unpickle_pure_python | 152 us                                                      | 150 us: 1.01x faster                                                     |
| pickle_pure_python   | 200 us                                                      | 198 us: 1.01x faster                                                     |
| xml_etree_generate   | 52.2 ms                                                     | 51.8 ms: 1.01x faster                                                    |
| json_dumps           | 7.56 ms                                                     | 7.60 ms: 1.01x slower                                                    |
| json_loads           | 12.9 us                                                     | 13.0 us: 1.01x slower                                                    |
| pickle               | 6.61 us                                                     | 6.73 us: 1.02x slower                                                    |
| pickle_list          | 2.68 us                                                     | 2.78 us: 1.04x slower                                                    |
| unpickle_list        | 2.55 us                                                     | 2.68 us: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                             |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf1-amd64-python-f3909b8bc83675b7ab09-3.11.3-f3909b8 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.3 ms: 1.04x faster                                                    |
| python_startup         | 18.7 ms                                                     | 18.4 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf1-amd64-python-f3909b8bc83675b7ab09-3.11.3-f3909b8 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 24.1 ms                                                     | 23.8 ms: 1.01x faster                                                    |
| mako            | 7.26 ms                                                     | 7.22 ms: 1.01x faster                                                    |
| genshi_text     | 17.0 ms                                                     | 17.3 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                       | 1.00x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf1-amd64-python-f3909b8bc83675b7ab09-3.11.3-f3909b8 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io          | 779 ms                                                      | 739 ms: 1.05x faster                                                     |
| xml_etree_parse        | 95.9 ms                                                     | 91.3 ms: 1.05x faster                                                    |
| coverage               | 55.9 ms                                                     | 53.2 ms: 1.05x faster                                                    |
| aiohttp                | 899 us                                                      | 857 us: 1.05x faster                                                     |
| dulwich_log            | 44.5 ms                                                     | 42.5 ms: 1.05x faster                                                    |
| create_gc_cycles       | 693 us                                                      | 664 us: 1.04x faster                                                     |
| raytrace               | 211 ms                                                      | 203 ms: 1.04x faster                                                     |
| float                  | 54.6 ms                                                     | 52.6 ms: 1.04x faster                                                    |
| comprehensions         | 15.9 us                                                     | 15.4 us: 1.04x faster                                                    |
| python_startup_no_site | 15.9 ms                                                     | 15.3 ms: 1.04x faster                                                    |
| sqlglot_transpile      | 1.16 ms                                                     | 1.13 ms: 1.03x faster                                                    |
| sqlglot_parse          | 952 us                                                      | 931 us: 1.02x faster                                                     |
| gc_traversal           | 1.46 ms                                                     | 1.43 ms: 1.02x faster                                                    |
| xml_etree_process      | 37.1 ms                                                     | 36.3 ms: 1.02x faster                                                    |
| xml_etree_iterparse    | 62.6 ms                                                     | 61.4 ms: 1.02x faster                                                    |
| tornado_http           | 91.8 ms                                                     | 90.1 ms: 1.02x faster                                                    |
| async_tree_none        | 320 ms                                                      | 314 ms: 1.02x faster                                                     |
| sympy_expand           | 295 ms                                                      | 290 ms: 1.02x faster                                                     |
| sqlalchemy_imperative  | 10.2 ms                                                     | 10.0 ms: 1.02x faster                                                    |
| thrift                 | 491 us                                                      | 482 us: 1.02x faster                                                     |
| deepcopy_reduce        | 2.07 us                                                     | 2.04 us: 1.02x faster                                                    |
| sympy_sum              | 99.9 ms                                                     | 98.4 ms: 1.02x faster                                                    |
| unpickle               | 8.09 us                                                     | 7.97 us: 1.02x faster                                                    |
| python_startup         | 18.7 ms                                                     | 18.4 ms: 1.01x faster                                                    |
| unpickle_pure_python   | 152 us                                                      | 150 us: 1.01x faster                                                     |
| deepcopy_memo          | 25.2 us                                                     | 24.8 us: 1.01x faster                                                    |
| sympy_integrate        | 13.8 ms                                                     | 13.6 ms: 1.01x faster                                                    |
| 2to3                   | 209 ms                                                      | 206 ms: 1.01x faster                                                     |
| docutils               | 1.60 sec                                                    | 1.58 sec: 1.01x faster                                                   |
| django_template        | 24.1 ms                                                     | 23.8 ms: 1.01x faster                                                    |
| pickle_pure_python     | 200 us                                                      | 198 us: 1.01x faster                                                     |
| deepcopy               | 246 us                                                      | 243 us: 1.01x faster                                                     |
| async_generators       | 178 ms                                                      | 176 ms: 1.01x faster                                                     |
| regex_compile          | 90.6 ms                                                     | 89.7 ms: 1.01x faster                                                    |
| pyflate                | 304 ms                                                      | 301 ms: 1.01x faster                                                     |
| xml_etree_generate     | 52.2 ms                                                     | 51.8 ms: 1.01x faster                                                    |
| pidigits               | 148 ms                                                      | 147 ms: 1.01x faster                                                     |
| bench_mp_pool          | 62.5 ms                                                     | 62.0 ms: 1.01x faster                                                    |
| mako                   | 7.26 ms                                                     | 7.22 ms: 1.01x faster                                                    |
| sqlglot_optimize       | 34.9 ms                                                     | 34.7 ms: 1.01x faster                                                    |
| richards               | 30.6 ms                                                     | 30.4 ms: 1.01x faster                                                    |
| spectral_norm          | 67.9 ms                                                     | 67.6 ms: 1.01x faster                                                    |
| bench_thread_pool      | 852 us                                                      | 848 us: 1.01x faster                                                     |
| sqlalchemy_declarative | 81.5 ms                                                     | 81.1 ms: 1.00x faster                                                    |
| flaskblogging          | 2.04 sec                                                    | 2.05 sec: 1.00x slower                                                   |
| json_dumps             | 7.56 ms                                                     | 7.60 ms: 1.01x slower                                                    |
| sqlite_synth           | 1.68 us                                                     | 1.69 us: 1.01x slower                                                    |
| json_loads             | 12.9 us                                                     | 13.0 us: 1.01x slower                                                    |
| logging_simple         | 6.61 us                                                     | 6.67 us: 1.01x slower                                                    |
| nqueens                | 64.9 ms                                                     | 65.6 ms: 1.01x slower                                                    |
| scimark_monte_carlo    | 44.6 ms                                                     | 45.1 ms: 1.01x slower                                                    |
| crypto_pyaes           | 47.6 ms                                                     | 48.2 ms: 1.01x slower                                                    |
| fannkuch               | 252 ms                                                      | 256 ms: 1.01x slower                                                     |
| deltablue              | 2.61 ms                                                     | 2.65 ms: 1.02x slower                                                    |
| pycparser              | 691 ms                                                      | 703 ms: 1.02x slower                                                     |
| pickle                 | 6.61 us                                                     | 6.73 us: 1.02x slower                                                    |
| go                     | 97.3 ms                                                     | 99.2 ms: 1.02x slower                                                    |
| pprint_pformat         | 1.04 sec                                                    | 1.06 sec: 1.02x slower                                                   |
| genshi_text            | 17.0 ms                                                     | 17.3 ms: 1.02x slower                                                    |
| pathlib                | 71.4 ms                                                     | 73.2 ms: 1.03x slower                                                    |
| pprint_safe_repr       | 512 ms                                                      | 526 ms: 1.03x slower                                                     |
| chameleon              | 5.11 ms                                                     | 5.27 ms: 1.03x slower                                                    |
| telco                  | 3.90 ms                                                     | 4.02 ms: 1.03x slower                                                    |
| regex_v8               | 13.8 ms                                                     | 14.3 ms: 1.03x slower                                                    |
| coroutines             | 14.6 ms                                                     | 15.1 ms: 1.03x slower                                                    |
| scimark_fft            | 178 ms                                                      | 185 ms: 1.03x slower                                                     |
| pickle_list            | 2.68 us                                                     | 2.78 us: 1.04x slower                                                    |
| chaos                  | 47.1 ms                                                     | 48.9 ms: 1.04x slower                                                    |
| regex_dna              | 115 ms                                                      | 120 ms: 1.04x slower                                                     |
| mdp                    | 1.67 sec                                                    | 1.74 sec: 1.04x slower                                                   |
| regex_effbot           | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                    |
| unpickle_list          | 2.55 us                                                     | 2.68 us: 1.05x slower                                                    |
| html5lib               | 37.5 ms                                                     | 39.8 ms: 1.06x slower                                                    |
| mypy2                  | 229 ms                                                      | 280 ms: 1.22x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                             |

Benchmark hidden because not significant (20): pylint, dask, async_tree_memoization, scimark_sor, nbody, scimark_lu, logging_format, async_tree_cpu_io_mixed, unpack_sequence, json, meteor_contest, sympy_str, hexiom, scimark_sparse_mat_mult, sqlglot_normalize, logging_silent, pickle_dict, generators, genshi_xml, asyncio_tcp
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 90.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
