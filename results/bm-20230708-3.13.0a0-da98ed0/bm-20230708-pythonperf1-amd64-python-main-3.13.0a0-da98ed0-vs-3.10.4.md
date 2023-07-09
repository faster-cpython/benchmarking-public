
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: da98ed0
- commit date: 2023-07-08
- overall geometric mean: 1.10x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf1-amd64-python-main-3.13.0a0-da98ed0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.68 sec: 1.13x faster                                     |
| tornado_http   | 109 ms                                                      | 98.1 ms: 1.11x faster                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf1-amd64-python-main-3.13.0a0-da98ed0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 56.9 ms: 1.06x faster                                      |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                       |
| nbody          | 69.3 ms                                                     | 81.2 ms: 1.17x slower                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf1-amd64-python-main-3.13.0a0-da98ed0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 132 ms                                                      | 119 ms: 1.11x faster                                       |
| regex_compile  | 103 ms                                                      | 94.6 ms: 1.09x faster                                      |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf1-amd64-python-main-3.13.0a0-da98ed0 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.79 ms: 1.47x faster                                      |
| pickle_pure_python   | 257 us                                                      | 210 us: 1.22x faster                                       |
| unpickle_pure_python | 171 us                                                      | 151 us: 1.14x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 91.7 ms: 1.11x faster                                      |
| unpickle             | 9.17 us                                                     | 8.57 us: 1.07x faster                                      |
| xml_etree_process    | 43.4 ms                                                     | 40.8 ms: 1.06x faster                                      |
| json_loads           | 14.2 us                                                     | 13.7 us: 1.03x faster                                      |
| tomli_loads          | 1.62 sec                                                    | 1.61 sec: 1.01x faster                                     |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.4 ms: 1.03x slower                                      |
| pickle               | 6.80 us                                                     | 7.10 us: 1.04x slower                                      |
| xml_etree_generate   | 54.5 ms                                                     | 58.9 ms: 1.08x slower                                      |
| pickle_list          | 2.59 us                                                     | 2.80 us: 1.08x slower                                      |
| pickle_dict          | 16.9 us                                                     | 19.1 us: 1.13x slower                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf1-amd64-python-main-3.13.0a0-da98ed0 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.0 ms: 1.10x slower                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf1-amd64-python-main-3.13.0a0-da98ed0 |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.63 ms: 1.15x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf1-amd64-python-main-3.13.0a0-da98ed0 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 97.8 us: 3.32x faster                                      |
| deltablue                | 4.17 ms                                                     | 2.38 ms: 1.75x faster                                      |
| mypy2                    | 352 ms                                                      | 223 ms: 1.58x faster                                       |
| json_dumps               | 8.50 ms                                                     | 5.79 ms: 1.47x faster                                      |
| raytrace                 | 271 ms                                                      | 185 ms: 1.46x faster                                       |
| async_tree_io            | 1.07 sec                                                    | 732 ms: 1.45x faster                                       |
| richards_super           | 51.7 ms                                                     | 35.6 ms: 1.45x faster                                      |
| async_tree_none          | 420 ms                                                      | 296 ms: 1.42x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 352 ms: 1.41x faster                                       |
| logging_silent           | 96.4 ns                                                     | 68.4 ns: 1.41x faster                                      |
| sqlglot_parse            | 1.22 ms                                                     | 896 us: 1.36x faster                                       |
| go                       | 136 ms                                                      | 100 ms: 1.36x faster                                       |
| richards                 | 41.2 ms                                                     | 31.5 ms: 1.31x faster                                      |
| chaos                    | 58.9 ms                                                     | 45.2 ms: 1.30x faster                                      |
| sqlglot_transpile        | 1.46 ms                                                     | 1.13 ms: 1.30x faster                                      |
| scimark_lu               | 85.4 ms                                                     | 66.0 ms: 1.30x faster                                      |
| asyncio_tcp              | 712 ms                                                      | 553 ms: 1.29x faster                                       |
| generators               | 31.6 ms                                                     | 25.0 ms: 1.26x faster                                      |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 488 ms: 1.25x faster                                       |
| crypto_pyaes             | 62.3 ms                                                     | 50.8 ms: 1.23x faster                                      |
| pickle_pure_python       | 257 us                                                      | 210 us: 1.22x faster                                       |
| hexiom                   | 5.52 ms                                                     | 4.57 ms: 1.21x faster                                      |
| pyflate                  | 387 ms                                                      | 327 ms: 1.18x faster                                       |
| spectral_norm            | 78.0 ms                                                     | 67.3 ms: 1.16x faster                                      |
| pycparser                | 868 ms                                                      | 750 ms: 1.16x faster                                       |
| mako                     | 8.80 ms                                                     | 7.63 ms: 1.15x faster                                      |
| mdp                      | 1.71 sec                                                    | 1.49 sec: 1.15x faster                                     |
| unpickle_pure_python     | 171 us                                                      | 151 us: 1.14x faster                                       |
| scimark_sor              | 105 ms                                                      | 92.9 ms: 1.13x faster                                      |
| docutils                 | 1.89 sec                                                    | 1.68 sec: 1.13x faster                                     |
| scimark_monte_carlo      | 55.9 ms                                                     | 49.7 ms: 1.12x faster                                      |
| tornado_http             | 109 ms                                                      | 98.1 ms: 1.11x faster                                      |
| xml_etree_parse          | 102 ms                                                      | 91.7 ms: 1.11x faster                                      |
| regex_dna                | 132 ms                                                      | 119 ms: 1.11x faster                                       |
| regex_compile            | 103 ms                                                      | 94.6 ms: 1.09x faster                                      |
| bench_thread_pool        | 946 us                                                      | 872 us: 1.08x faster                                       |
| sqlglot_optimize         | 39.0 ms                                                     | 36.1 ms: 1.08x faster                                      |
| deepcopy_memo            | 28.5 us                                                     | 26.5 us: 1.07x faster                                      |
| unpickle                 | 9.17 us                                                     | 8.57 us: 1.07x faster                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.13 sec: 1.07x faster                                     |
| create_gc_cycles         | 782 us                                                      | 732 us: 1.07x faster                                       |
| pprint_safe_repr         | 589 ms                                                      | 552 ms: 1.07x faster                                       |
| xml_etree_process        | 43.4 ms                                                     | 40.8 ms: 1.06x faster                                      |
| float                    | 60.2 ms                                                     | 56.9 ms: 1.06x faster                                      |
| json                     | 3.05 ms                                                     | 2.89 ms: 1.06x faster                                      |
| coroutines               | 15.9 ms                                                     | 15.2 ms: 1.05x faster                                      |
| sqlite_synth             | 1.84 us                                                     | 1.76 us: 1.05x faster                                      |
| sqlglot_normalize        | 202 ms                                                      | 193 ms: 1.05x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                      |
| dulwich_log              | 47.6 ms                                                     | 45.8 ms: 1.04x faster                                      |
| json_loads               | 14.2 us                                                     | 13.7 us: 1.03x faster                                      |
| comprehensions           | 16.0 us                                                     | 15.5 us: 1.03x faster                                      |
| nqueens                  | 67.0 ms                                                     | 66.1 ms: 1.01x faster                                      |
| tomli_loads              | 1.62 sec                                                    | 1.61 sec: 1.01x faster                                     |
| deepcopy                 | 255 us                                                      | 258 us: 1.01x slower                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.71 ms: 1.02x slower                                      |
| xml_etree_iterparse      | 63.5 ms                                                     | 65.4 ms: 1.03x slower                                      |
| pidigits                 | 145 ms                                                      | 150 ms: 1.03x slower                                       |
| pickle                   | 6.80 us                                                     | 7.10 us: 1.04x slower                                      |
| meteor_contest           | 72.5 ms                                                     | 76.6 ms: 1.06x slower                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.28 us: 1.06x slower                                      |
| scimark_fft              | 193 ms                                                      | 205 ms: 1.06x slower                                       |
| pathlib                  | 77.4 ms                                                     | 83.1 ms: 1.07x slower                                      |
| xml_etree_generate       | 54.5 ms                                                     | 58.9 ms: 1.08x slower                                      |
| fannkuch                 | 258 ms                                                      | 279 ms: 1.08x slower                                       |
| pickle_list              | 2.59 us                                                     | 2.80 us: 1.08x slower                                      |
| async_generators         | 224 ms                                                      | 244 ms: 1.09x slower                                       |
| gc_traversal             | 1.34 ms                                                     | 1.47 ms: 1.10x slower                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.0 ms: 1.10x slower                                      |
| bench_mp_pool            | 60.7 ms                                                     | 67.0 ms: 1.10x slower                                      |
| unpack_sequence          | 37.8 ns                                                     | 42.1 ns: 1.11x slower                                      |
| logging_format           | 6.66 us                                                     | 7.48 us: 1.12x slower                                      |
| pickle_dict              | 16.9 us                                                     | 19.1 us: 1.13x slower                                      |
| logging_simple           | 6.20 us                                                     | 7.01 us: 1.13x slower                                      |
| nbody                    | 69.3 ms                                                     | 81.2 ms: 1.17x slower                                      |
| telco                    | 3.78 ms                                                     | 4.48 ms: 1.18x slower                                      |
| dask                     | 305 ms                                                      | 394 ms: 1.29x slower                                       |
| coverage                 | 40.0 ms                                                     | 52.8 ms: 1.32x slower                                      |
| Geometric mean           | (ref)                                                       | 1.10x faster                                               |

Benchmark hidden because not significant (4): python_startup, unpickle_list, asyncio_tcp_ssl, regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
