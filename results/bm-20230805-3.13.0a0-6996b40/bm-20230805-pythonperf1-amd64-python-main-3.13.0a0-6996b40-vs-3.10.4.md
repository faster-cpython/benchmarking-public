
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 6996b40
- commit date: 2023-08-05
- overall geometric mean: 1.10x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.73 sec: 1.10x faster                                     |
| tornado_http   | 109 ms                                                      | 90.0 ms: 1.21x faster                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 59.2 ms: 1.02x faster                                      |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                       |
| nbody          | 69.3 ms                                                     | 83.0 ms: 1.20x slower                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 132 ms                                                      | 122 ms: 1.08x faster                                       |
| regex_compile  | 103 ms                                                      | 96.8 ms: 1.07x faster                                      |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.83 ms: 1.46x faster                                      |
| pickle_pure_python   | 257 us                                                      | 205 us: 1.25x faster                                       |
| unpickle_pure_python | 171 us                                                      | 151 us: 1.13x faster                                       |
| unpickle             | 9.17 us                                                     | 8.32 us: 1.10x faster                                      |
| xml_etree_process    | 43.4 ms                                                     | 40.4 ms: 1.08x faster                                      |
| xml_etree_parse      | 102 ms                                                      | 99.1 ms: 1.03x faster                                      |
| json_loads           | 14.2 us                                                     | 13.9 us: 1.02x faster                                      |
| tomli_loads          | 1.62 sec                                                    | 1.66 sec: 1.03x slower                                     |
| pickle               | 6.80 us                                                     | 7.07 us: 1.04x slower                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 66.6 ms: 1.05x slower                                      |
| xml_etree_generate   | 54.5 ms                                                     | 57.8 ms: 1.06x slower                                      |
| pickle_list          | 2.59 us                                                     | 2.80 us: 1.08x slower                                      |
| pickle_dict          | 16.9 us                                                     | 18.4 us: 1.09x slower                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.4 ms: 1.03x faster                                      |
| python_startup_no_site | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                      |
| Geometric mean         | (ref)                                                       | 1.01x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40 |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.92 ms: 1.11x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf1-amd64-python-main-3.13.0a0-6996b40 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 103 us: 3.16x faster                                       |
| deltablue                | 4.17 ms                                                     | 2.44 ms: 1.71x faster                                      |
| mypy2                    | 352 ms                                                      | 225 ms: 1.56x faster                                       |
| richards_super           | 51.7 ms                                                     | 34.5 ms: 1.50x faster                                      |
| json_dumps               | 8.50 ms                                                     | 5.83 ms: 1.46x faster                                      |
| logging_silent           | 96.4 ns                                                     | 68.2 ns: 1.41x faster                                      |
| raytrace                 | 271 ms                                                      | 193 ms: 1.41x faster                                       |
| asyncio_tcp              | 712 ms                                                      | 508 ms: 1.40x faster                                       |
| async_tree_io            | 1.07 sec                                                    | 779 ms: 1.37x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 364 ms: 1.37x faster                                       |
| scimark_lu               | 85.4 ms                                                     | 63.1 ms: 1.35x faster                                      |
| sqlglot_parse            | 1.22 ms                                                     | 901 us: 1.35x faster                                       |
| async_tree_none          | 420 ms                                                      | 313 ms: 1.34x faster                                       |
| richards                 | 41.2 ms                                                     | 31.0 ms: 1.33x faster                                      |
| go                       | 136 ms                                                      | 103 ms: 1.33x faster                                       |
| crypto_pyaes             | 62.3 ms                                                     | 47.1 ms: 1.32x faster                                      |
| chaos                    | 58.9 ms                                                     | 44.8 ms: 1.31x faster                                      |
| sqlglot_transpile        | 1.46 ms                                                     | 1.11 ms: 1.31x faster                                      |
| pickle_pure_python       | 257 us                                                      | 205 us: 1.25x faster                                       |
| tornado_http             | 109 ms                                                      | 90.0 ms: 1.21x faster                                      |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 505 ms: 1.21x faster                                       |
| scimark_sor              | 105 ms                                                      | 87.2 ms: 1.20x faster                                      |
| pyflate                  | 387 ms                                                      | 324 ms: 1.20x faster                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 47.2 ms: 1.18x faster                                      |
| hexiom                   | 5.52 ms                                                     | 4.70 ms: 1.17x faster                                      |
| generators               | 31.6 ms                                                     | 27.0 ms: 1.17x faster                                      |
| pycparser                | 868 ms                                                      | 755 ms: 1.15x faster                                       |
| unpickle_pure_python     | 171 us                                                      | 151 us: 1.13x faster                                       |
| mako                     | 8.80 ms                                                     | 7.92 ms: 1.11x faster                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.09 sec: 1.10x faster                                     |
| unpickle                 | 9.17 us                                                     | 8.32 us: 1.10x faster                                      |
| spectral_norm            | 78.0 ms                                                     | 71.0 ms: 1.10x faster                                      |
| docutils                 | 1.89 sec                                                    | 1.73 sec: 1.10x faster                                     |
| deepcopy_memo            | 28.5 us                                                     | 26.1 us: 1.09x faster                                      |
| pprint_safe_repr         | 589 ms                                                      | 542 ms: 1.09x faster                                       |
| sqlglot_optimize         | 39.0 ms                                                     | 36.0 ms: 1.08x faster                                      |
| regex_dna                | 132 ms                                                      | 122 ms: 1.08x faster                                       |
| xml_etree_process        | 43.4 ms                                                     | 40.4 ms: 1.08x faster                                      |
| bench_thread_pool        | 946 us                                                      | 883 us: 1.07x faster                                       |
| mdp                      | 1.71 sec                                                    | 1.60 sec: 1.07x faster                                     |
| regex_compile            | 103 ms                                                      | 96.8 ms: 1.07x faster                                      |
| json                     | 3.05 ms                                                     | 2.92 ms: 1.04x faster                                      |
| create_gc_cycles         | 782 us                                                      | 752 us: 1.04x faster                                       |
| comprehensions           | 16.0 us                                                     | 15.4 us: 1.04x faster                                      |
| nqueens                  | 67.0 ms                                                     | 65.1 ms: 1.03x faster                                      |
| python_startup           | 20.0 ms                                                     | 19.4 ms: 1.03x faster                                      |
| xml_etree_parse          | 102 ms                                                      | 99.1 ms: 1.03x faster                                      |
| sqlite_synth             | 1.84 us                                                     | 1.80 us: 1.02x faster                                      |
| json_loads               | 14.2 us                                                     | 13.9 us: 1.02x faster                                      |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                      |
| sqlglot_normalize        | 202 ms                                                      | 198 ms: 1.02x faster                                       |
| float                    | 60.2 ms                                                     | 59.2 ms: 1.02x faster                                      |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.62 ms: 1.02x faster                                      |
| scimark_fft              | 193 ms                                                      | 192 ms: 1.01x faster                                       |
| dulwich_log              | 47.6 ms                                                     | 48.1 ms: 1.01x slower                                      |
| tomli_loads              | 1.62 sec                                                    | 1.66 sec: 1.03x slower                                     |
| pidigits                 | 145 ms                                                      | 150 ms: 1.03x slower                                       |
| unpack_sequence          | 37.8 ns                                                     | 39.2 ns: 1.04x slower                                      |
| pickle                   | 6.80 us                                                     | 7.07 us: 1.04x slower                                      |
| xml_etree_iterparse      | 63.5 ms                                                     | 66.6 ms: 1.05x slower                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.28 us: 1.06x slower                                      |
| python_startup_no_site   | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                      |
| meteor_contest           | 72.5 ms                                                     | 76.9 ms: 1.06x slower                                      |
| xml_etree_generate       | 54.5 ms                                                     | 57.8 ms: 1.06x slower                                      |
| pickle_list              | 2.59 us                                                     | 2.80 us: 1.08x slower                                      |
| pickle_dict              | 16.9 us                                                     | 18.4 us: 1.09x slower                                      |
| pathlib                  | 77.4 ms                                                     | 84.3 ms: 1.09x slower                                      |
| async_generators         | 224 ms                                                      | 250 ms: 1.12x slower                                       |
| bench_mp_pool            | 60.7 ms                                                     | 67.7 ms: 1.12x slower                                      |
| logging_simple           | 6.20 us                                                     | 7.05 us: 1.14x slower                                      |
| gc_traversal             | 1.34 ms                                                     | 1.54 ms: 1.14x slower                                      |
| logging_format           | 6.66 us                                                     | 7.75 us: 1.16x slower                                      |
| nbody                    | 69.3 ms                                                     | 83.0 ms: 1.20x slower                                      |
| dask                     | 305 ms                                                      | 389 ms: 1.27x slower                                       |
| telco                    | 3.78 ms                                                     | 5.16 ms: 1.36x slower                                      |
| coverage                 | 40.0 ms                                                     | 55.1 ms: 1.38x slower                                      |
| Geometric mean           | (ref)                                                       | 1.10x faster                                               |

Benchmark hidden because not significant (6): regex_v8, fannkuch, deepcopy, coroutines, asyncio_tcp_ssl, unpickle_list
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
