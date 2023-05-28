
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 3a5be87
- commit date: 2023-05-28
- overall geometric mean: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.61 sec: 1.18x faster                                     |
| html5lib       | 46.5 ms                                                     | 35.8 ms: 1.30x faster                                      |
| tornado_http   | 109 ms                                                      | 89.4 ms: 1.22x faster                                      |
| Geometric mean | (ref)                                                       | 1.23x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 52.2 ms: 1.15x faster                                      |
| nbody          | 69.3 ms                                                     | 70.5 ms: 1.02x slower                                      |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 85.4 ms: 1.21x faster                                      |
| regex_dna      | 132 ms                                                      | 124 ms: 1.07x faster                                       |
| regex_v8       | 15.0 ms                                                     | 14.3 ms: 1.05x faster                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.64 ms: 1.51x faster                                      |
| pickle_pure_python   | 257 us                                                      | 190 us: 1.35x faster                                       |
| unpickle_pure_python | 171 us                                                      | 132 us: 1.30x faster                                       |
| tomli_loads          | 1.62 sec                                                    | 1.34 sec: 1.21x faster                                     |
| xml_etree_process    | 43.4 ms                                                     | 37.1 ms: 1.17x faster                                      |
| unpickle             | 9.17 us                                                     | 8.04 us: 1.14x faster                                      |
| xml_etree_parse      | 102 ms                                                      | 91.7 ms: 1.11x faster                                      |
| json_loads           | 14.2 us                                                     | 13.4 us: 1.06x faster                                      |
| xml_etree_generate   | 54.5 ms                                                     | 54.8 ms: 1.01x slower                                      |
| pickle               | 6.80 us                                                     | 6.98 us: 1.03x slower                                      |
| pickle_dict          | 16.9 us                                                     | 18.3 us: 1.08x slower                                      |
| pickle_list          | 2.59 us                                                     | 2.82 us: 1.09x slower                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                               |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.0 ms: 1.05x faster                                      |
| python_startup_no_site | 15.5 ms                                                     | 16.3 ms: 1.05x slower                                      |
| Geometric mean         | (ref)                                                       | 1.00x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako           | 8.80 ms                                                     | 6.62 ms: 1.33x faster                                      |
| genshi_text    | 19.0 ms                                                     | 15.3 ms: 1.24x faster                                      |
| genshi_xml     | 40.5 ms                                                     | 33.4 ms: 1.21x faster                                      |
| Geometric mean | (ref)                                                       | 1.26x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 88.9 us: 3.65x faster                                      |
| deltablue                | 4.17 ms                                                     | 2.08 ms: 2.00x faster                                      |
| richards_super           | 51.7 ms                                                     | 28.8 ms: 1.80x faster                                      |
| mypy2                    | 352 ms                                                      | 213 ms: 1.65x faster                                       |
| richards                 | 41.2 ms                                                     | 25.0 ms: 1.65x faster                                      |
| logging_silent           | 96.4 ns                                                     | 60.3 ns: 1.60x faster                                      |
| go                       | 136 ms                                                      | 86.0 ms: 1.58x faster                                      |
| sqlglot_parse            | 1.22 ms                                                     | 785 us: 1.55x faster                                       |
| json_dumps               | 8.50 ms                                                     | 5.64 ms: 1.51x faster                                      |
| sqlglot_transpile        | 1.46 ms                                                     | 989 us: 1.48x faster                                       |
| scimark_lu               | 85.4 ms                                                     | 58.0 ms: 1.47x faster                                      |
| generators               | 31.6 ms                                                     | 21.5 ms: 1.47x faster                                      |
| asyncio_tcp              | 712 ms                                                      | 485 ms: 1.47x faster                                       |
| raytrace                 | 271 ms                                                      | 186 ms: 1.46x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 342 ms: 1.46x faster                                       |
| async_tree_io            | 1.07 sec                                                    | 734 ms: 1.45x faster                                       |
| async_tree_none          | 420 ms                                                      | 294 ms: 1.43x faster                                       |
| hexiom                   | 5.52 ms                                                     | 3.92 ms: 1.41x faster                                      |
| chaos                    | 58.9 ms                                                     | 42.7 ms: 1.38x faster                                      |
| pickle_pure_python       | 257 us                                                      | 190 us: 1.35x faster                                       |
| scimark_sor              | 105 ms                                                      | 77.7 ms: 1.35x faster                                      |
| pyflate                  | 387 ms                                                      | 288 ms: 1.34x faster                                       |
| mako                     | 8.80 ms                                                     | 6.62 ms: 1.33x faster                                      |
| crypto_pyaes             | 62.3 ms                                                     | 47.4 ms: 1.32x faster                                      |
| pycparser                | 868 ms                                                      | 661 ms: 1.31x faster                                       |
| unpickle_pure_python     | 171 us                                                      | 132 us: 1.30x faster                                       |
| html5lib                 | 46.5 ms                                                     | 35.8 ms: 1.30x faster                                      |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 473 ms: 1.29x faster                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 44.6 ms: 1.25x faster                                      |
| spectral_norm            | 78.0 ms                                                     | 62.4 ms: 1.25x faster                                      |
| genshi_text              | 19.0 ms                                                     | 15.3 ms: 1.24x faster                                      |
| deepcopy_memo            | 28.5 us                                                     | 23.1 us: 1.24x faster                                      |
| tornado_http             | 109 ms                                                      | 89.4 ms: 1.22x faster                                      |
| genshi_xml               | 40.5 ms                                                     | 33.4 ms: 1.21x faster                                      |
| regex_compile            | 103 ms                                                      | 85.4 ms: 1.21x faster                                      |
| tomli_loads              | 1.62 sec                                                    | 1.34 sec: 1.21x faster                                     |
| pprint_pformat           | 1.21 sec                                                    | 1.02 sec: 1.18x faster                                     |
| docutils                 | 1.89 sec                                                    | 1.61 sec: 1.18x faster                                     |
| pprint_safe_repr         | 589 ms                                                      | 501 ms: 1.18x faster                                       |
| xml_etree_process        | 43.4 ms                                                     | 37.1 ms: 1.17x faster                                      |
| sqlglot_optimize         | 39.0 ms                                                     | 33.4 ms: 1.17x faster                                      |
| bench_thread_pool        | 946 us                                                      | 819 us: 1.16x faster                                       |
| coroutines               | 15.9 ms                                                     | 13.8 ms: 1.15x faster                                      |
| float                    | 60.2 ms                                                     | 52.2 ms: 1.15x faster                                      |
| mdp                      | 1.71 sec                                                    | 1.49 sec: 1.15x faster                                     |
| comprehensions           | 16.0 us                                                     | 13.9 us: 1.15x faster                                      |
| unpickle                 | 9.17 us                                                     | 8.04 us: 1.14x faster                                      |
| create_gc_cycles         | 782 us                                                      | 693 us: 1.13x faster                                       |
| dulwich_log              | 47.6 ms                                                     | 42.3 ms: 1.13x faster                                      |
| nqueens                  | 67.0 ms                                                     | 60.0 ms: 1.12x faster                                      |
| sqlglot_normalize        | 202 ms                                                      | 181 ms: 1.12x faster                                       |
| xml_etree_parse          | 102 ms                                                      | 91.7 ms: 1.11x faster                                      |
| deepcopy                 | 255 us                                                      | 233 us: 1.09x faster                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.45 ms: 1.09x faster                                      |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 1.87 sec: 1.09x faster                                     |
| fannkuch                 | 258 ms                                                      | 240 ms: 1.07x faster                                       |
| scimark_fft              | 193 ms                                                      | 180 ms: 1.07x faster                                       |
| regex_dna                | 132 ms                                                      | 124 ms: 1.07x faster                                       |
| sqlite_synth             | 1.84 us                                                     | 1.73 us: 1.06x faster                                      |
| json_loads               | 14.2 us                                                     | 13.4 us: 1.06x faster                                      |
| python_startup           | 20.0 ms                                                     | 19.0 ms: 1.05x faster                                      |
| json                     | 3.05 ms                                                     | 2.89 ms: 1.05x faster                                      |
| regex_v8                 | 15.0 ms                                                     | 14.3 ms: 1.05x faster                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.05 us: 1.05x faster                                      |
| meteor_contest           | 72.5 ms                                                     | 71.9 ms: 1.01x faster                                      |
| xml_etree_generate       | 54.5 ms                                                     | 54.8 ms: 1.01x slower                                      |
| logging_format           | 6.66 us                                                     | 6.73 us: 1.01x slower                                      |
| nbody                    | 69.3 ms                                                     | 70.5 ms: 1.02x slower                                      |
| logging_simple           | 6.20 us                                                     | 6.32 us: 1.02x slower                                      |
| pickle                   | 6.80 us                                                     | 6.98 us: 1.03x slower                                      |
| pidigits                 | 145 ms                                                      | 150 ms: 1.03x slower                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.3 ms: 1.05x slower                                      |
| async_generators         | 224 ms                                                      | 237 ms: 1.06x slower                                       |
| pickle_dict              | 16.9 us                                                     | 18.3 us: 1.08x slower                                      |
| unpack_sequence          | 37.8 ns                                                     | 41.0 ns: 1.08x slower                                      |
| gc_traversal             | 1.34 ms                                                     | 1.46 ms: 1.09x slower                                      |
| pickle_list              | 2.59 us                                                     | 2.82 us: 1.09x slower                                      |
| bench_mp_pool            | 60.7 ms                                                     | 67.4 ms: 1.11x slower                                      |
| pathlib                  | 77.4 ms                                                     | 86.0 ms: 1.11x slower                                      |
| telco                    | 3.78 ms                                                     | 4.26 ms: 1.13x slower                                      |
| coverage                 | 40.0 ms                                                     | 52.7 ms: 1.32x slower                                      |
| Geometric mean           | (ref)                                                       | 1.20x faster                                               |

Benchmark hidden because not significant (3): unpickle_list, regex_effbot, xml_etree_iterparse
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
