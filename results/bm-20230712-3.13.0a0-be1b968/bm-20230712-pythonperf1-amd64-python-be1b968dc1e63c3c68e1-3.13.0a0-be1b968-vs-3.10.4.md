
# Results vs. 3.10.4

- fork: python
- ref: be1b968dc1e63c3c68e1
- machine: windows-amd64
- commit hash: be1b968
- commit date: 2023-07-12
- overall geometric mean: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                                     |
| tornado_http   | 109 ms                                                      | 89.8 ms: 1.21x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 56.9 ms: 1.06x faster                                                      |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                                       |
| nbody          | 69.3 ms                                                     | 80.4 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 93.7 ms: 1.10x faster                                                      |
| regex_dna      | 132 ms                                                      | 120 ms: 1.09x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.68 ms: 1.50x faster                                                      |
| pickle_pure_python   | 257 us                                                      | 204 us: 1.26x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 146 us: 1.17x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.13 us: 1.13x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 90.6 ms: 1.12x faster                                                      |
| xml_etree_process    | 43.4 ms                                                     | 39.3 ms: 1.11x faster                                                      |
| json_loads           | 14.2 us                                                     | 13.5 us: 1.05x faster                                                      |
| tomli_loads          | 1.62 sec                                                    | 1.59 sec: 1.02x faster                                                     |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.1 ms: 1.02x slower                                                      |
| xml_etree_generate   | 54.5 ms                                                     | 56.9 ms: 1.04x slower                                                      |
| pickle               | 6.80 us                                                     | 7.27 us: 1.07x slower                                                      |
| pickle_list          | 2.59 us                                                     | 2.82 us: 1.09x slower                                                      |
| pickle_dict          | 16.9 us                                                     | 18.8 us: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.3 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.68 ms: 1.15x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 98.7 us: 3.29x faster                                                      |
| deltablue                | 4.17 ms                                                     | 2.28 ms: 1.83x faster                                                      |
| mypy2                    | 352 ms                                                      | 221 ms: 1.59x faster                                                       |
| richards_super           | 51.7 ms                                                     | 34.2 ms: 1.51x faster                                                      |
| json_dumps               | 8.50 ms                                                     | 5.68 ms: 1.50x faster                                                      |
| asyncio_tcp              | 712 ms                                                      | 480 ms: 1.48x faster                                                       |
| raytrace                 | 271 ms                                                      | 184 ms: 1.47x faster                                                       |
| logging_silent           | 96.4 ns                                                     | 65.7 ns: 1.47x faster                                                      |
| async_tree_io            | 1.07 sec                                                    | 739 ms: 1.44x faster                                                       |
| async_tree_memoization   | 497 ms                                                      | 351 ms: 1.42x faster                                                       |
| async_tree_none          | 420 ms                                                      | 300 ms: 1.40x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 870 us: 1.40x faster                                                       |
| go                       | 136 ms                                                      | 99.6 ms: 1.37x faster                                                      |
| scimark_lu               | 85.4 ms                                                     | 62.9 ms: 1.36x faster                                                      |
| richards                 | 41.2 ms                                                     | 30.4 ms: 1.36x faster                                                      |
| sqlglot_transpile        | 1.46 ms                                                     | 1.10 ms: 1.33x faster                                                      |
| chaos                    | 58.9 ms                                                     | 44.3 ms: 1.33x faster                                                      |
| crypto_pyaes             | 62.3 ms                                                     | 47.1 ms: 1.32x faster                                                      |
| pickle_pure_python       | 257 us                                                      | 204 us: 1.26x faster                                                       |
| generators               | 31.6 ms                                                     | 25.5 ms: 1.24x faster                                                      |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 492 ms: 1.24x faster                                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 45.3 ms: 1.23x faster                                                      |
| hexiom                   | 5.52 ms                                                     | 4.49 ms: 1.23x faster                                                      |
| tornado_http             | 109 ms                                                      | 89.8 ms: 1.21x faster                                                      |
| pyflate                  | 387 ms                                                      | 322 ms: 1.20x faster                                                       |
| mdp                      | 1.71 sec                                                    | 1.46 sec: 1.17x faster                                                     |
| scimark_sor              | 105 ms                                                      | 89.3 ms: 1.17x faster                                                      |
| unpickle_pure_python     | 171 us                                                      | 146 us: 1.17x faster                                                       |
| mako                     | 8.80 ms                                                     | 7.68 ms: 1.15x faster                                                      |
| bench_thread_pool        | 946 us                                                      | 835 us: 1.13x faster                                                       |
| docutils                 | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                                     |
| unpickle                 | 9.17 us                                                     | 8.13 us: 1.13x faster                                                      |
| xml_etree_parse          | 102 ms                                                      | 90.6 ms: 1.12x faster                                                      |
| spectral_norm            | 78.0 ms                                                     | 69.9 ms: 1.12x faster                                                      |
| xml_etree_process        | 43.4 ms                                                     | 39.3 ms: 1.11x faster                                                      |
| regex_compile            | 103 ms                                                      | 93.7 ms: 1.10x faster                                                      |
| pycparser                | 868 ms                                                      | 787 ms: 1.10x faster                                                       |
| regex_dna                | 132 ms                                                      | 120 ms: 1.09x faster                                                       |
| python_startup           | 20.0 ms                                                     | 18.3 ms: 1.09x faster                                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.11 sec: 1.09x faster                                                     |
| sqlglot_optimize         | 39.0 ms                                                     | 36.0 ms: 1.08x faster                                                      |
| pprint_safe_repr         | 589 ms                                                      | 545 ms: 1.08x faster                                                       |
| deepcopy_memo            | 28.5 us                                                     | 26.5 us: 1.08x faster                                                      |
| create_gc_cycles         | 782 us                                                      | 728 us: 1.07x faster                                                       |
| json                     | 3.05 ms                                                     | 2.85 ms: 1.07x faster                                                      |
| dulwich_log              | 47.6 ms                                                     | 44.6 ms: 1.07x faster                                                      |
| nqueens                  | 67.0 ms                                                     | 63.3 ms: 1.06x faster                                                      |
| float                    | 60.2 ms                                                     | 56.9 ms: 1.06x faster                                                      |
| sqlglot_normalize        | 202 ms                                                      | 192 ms: 1.05x faster                                                       |
| json_loads               | 14.2 us                                                     | 13.5 us: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                      |
| sqlite_synth             | 1.84 us                                                     | 1.77 us: 1.04x faster                                                      |
| coroutines               | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.59 ms: 1.03x faster                                                      |
| comprehensions           | 16.0 us                                                     | 15.6 us: 1.03x faster                                                      |
| tomli_loads              | 1.62 sec                                                    | 1.59 sec: 1.02x faster                                                     |
| deepcopy                 | 255 us                                                      | 250 us: 1.02x faster                                                       |
| scimark_fft              | 193 ms                                                      | 191 ms: 1.01x faster                                                       |
| pathlib                  | 77.4 ms                                                     | 78.7 ms: 1.02x slower                                                      |
| xml_etree_iterparse      | 63.5 ms                                                     | 65.1 ms: 1.02x slower                                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.22 us: 1.03x slower                                                      |
| pidigits                 | 145 ms                                                      | 151 ms: 1.04x slower                                                       |
| fannkuch                 | 258 ms                                                      | 267 ms: 1.04x slower                                                       |
| xml_etree_generate       | 54.5 ms                                                     | 56.9 ms: 1.04x slower                                                      |
| meteor_contest           | 72.5 ms                                                     | 75.8 ms: 1.05x slower                                                      |
| pickle                   | 6.80 us                                                     | 7.27 us: 1.07x slower                                                      |
| bench_mp_pool            | 60.7 ms                                                     | 65.4 ms: 1.08x slower                                                      |
| pickle_list              | 2.59 us                                                     | 2.82 us: 1.09x slower                                                      |
| async_generators         | 224 ms                                                      | 244 ms: 1.09x slower                                                       |
| gc_traversal             | 1.34 ms                                                     | 1.48 ms: 1.10x slower                                                      |
| logging_format           | 6.66 us                                                     | 7.38 us: 1.11x slower                                                      |
| logging_simple           | 6.20 us                                                     | 6.88 us: 1.11x slower                                                      |
| pickle_dict              | 16.9 us                                                     | 18.8 us: 1.11x slower                                                      |
| unpack_sequence          | 37.8 ns                                                     | 42.6 ns: 1.13x slower                                                      |
| telco                    | 3.78 ms                                                     | 4.34 ms: 1.15x slower                                                      |
| nbody                    | 69.3 ms                                                     | 80.4 ms: 1.16x slower                                                      |
| dask                     | 305 ms                                                      | 387 ms: 1.27x slower                                                       |
| coverage                 | 40.0 ms                                                     | 52.7 ms: 1.32x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (4): unpickle_list, python_startup_no_site, asyncio_tcp_ssl, regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
