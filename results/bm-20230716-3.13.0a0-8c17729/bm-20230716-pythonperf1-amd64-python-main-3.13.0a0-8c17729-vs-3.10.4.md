
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 8c17729
- commit date: 2023-07-16
- overall geometric mean: 1.13x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf1-amd64-python-main-3.13.0a0-8c17729 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                     |
| tornado_http   | 109 ms                                                      | 89.4 ms: 1.22x faster                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf1-amd64-python-main-3.13.0a0-8c17729 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 56.1 ms: 1.07x faster                                      |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                       |
| nbody          | 69.3 ms                                                     | 76.8 ms: 1.11x slower                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf1-amd64-python-main-3.13.0a0-8c17729 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 93.4 ms: 1.11x faster                                      |
| regex_dna      | 132 ms                                                      | 120 ms: 1.10x faster                                       |
| regex_v8       | 15.0 ms                                                     | 14.0 ms: 1.08x faster                                      |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf1-amd64-python-main-3.13.0a0-8c17729 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.75 ms: 1.48x faster                                      |
| pickle_pure_python   | 257 us                                                      | 201 us: 1.28x faster                                       |
| unpickle_pure_python | 171 us                                                      | 145 us: 1.18x faster                                       |
| xml_etree_process    | 43.4 ms                                                     | 39.2 ms: 1.11x faster                                      |
| unpickle             | 9.17 us                                                     | 8.38 us: 1.10x faster                                      |
| xml_etree_parse      | 102 ms                                                      | 93.8 ms: 1.08x faster                                      |
| json_loads           | 14.2 us                                                     | 13.6 us: 1.04x faster                                      |
| unpickle_list        | 2.81 us                                                     | 2.77 us: 1.01x faster                                      |
| pickle               | 6.80 us                                                     | 6.98 us: 1.03x slower                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.6 ms: 1.03x slower                                      |
| xml_etree_generate   | 54.5 ms                                                     | 56.8 ms: 1.04x slower                                      |
| pickle_list          | 2.59 us                                                     | 2.72 us: 1.05x slower                                      |
| pickle_dict          | 16.9 us                                                     | 18.0 us: 1.07x slower                                      |
| Geometric mean       | (ref)                                                       | 1.07x faster                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf1-amd64-python-main-3.13.0a0-8c17729 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.3 ms: 1.09x faster                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf1-amd64-python-main-3.13.0a0-8c17729 |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.43 ms: 1.18x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf1-amd64-python-main-3.13.0a0-8c17729 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 99.6 us: 3.26x faster                                      |
| deltablue                | 4.17 ms                                                     | 2.28 ms: 1.83x faster                                      |
| mypy2                    | 352 ms                                                      | 219 ms: 1.60x faster                                       |
| richards_super           | 51.7 ms                                                     | 34.7 ms: 1.49x faster                                      |
| asyncio_tcp              | 712 ms                                                      | 481 ms: 1.48x faster                                       |
| logging_silent           | 96.4 ns                                                     | 65.1 ns: 1.48x faster                                      |
| json_dumps               | 8.50 ms                                                     | 5.75 ms: 1.48x faster                                      |
| raytrace                 | 271 ms                                                      | 186 ms: 1.46x faster                                       |
| async_tree_io            | 1.07 sec                                                    | 733 ms: 1.45x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 348 ms: 1.43x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 853 us: 1.43x faster                                       |
| async_tree_none          | 420 ms                                                      | 297 ms: 1.42x faster                                       |
| go                       | 136 ms                                                      | 98.3 ms: 1.38x faster                                      |
| crypto_pyaes             | 62.3 ms                                                     | 45.4 ms: 1.37x faster                                      |
| scimark_lu               | 85.4 ms                                                     | 63.0 ms: 1.36x faster                                      |
| sqlglot_transpile        | 1.46 ms                                                     | 1.08 ms: 1.35x faster                                      |
| chaos                    | 58.9 ms                                                     | 43.7 ms: 1.35x faster                                      |
| richards                 | 41.2 ms                                                     | 30.7 ms: 1.34x faster                                      |
| generators               | 31.6 ms                                                     | 24.2 ms: 1.30x faster                                      |
| pickle_pure_python       | 257 us                                                      | 201 us: 1.28x faster                                       |
| hexiom                   | 5.52 ms                                                     | 4.38 ms: 1.26x faster                                      |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 488 ms: 1.25x faster                                       |
| pyflate                  | 387 ms                                                      | 313 ms: 1.24x faster                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 45.4 ms: 1.23x faster                                      |
| tornado_http             | 109 ms                                                      | 89.4 ms: 1.22x faster                                      |
| scimark_sor              | 105 ms                                                      | 86.3 ms: 1.22x faster                                      |
| mako                     | 8.80 ms                                                     | 7.43 ms: 1.18x faster                                      |
| pycparser                | 868 ms                                                      | 733 ms: 1.18x faster                                       |
| unpickle_pure_python     | 171 us                                                      | 145 us: 1.18x faster                                       |
| mdp                      | 1.71 sec                                                    | 1.49 sec: 1.15x faster                                     |
| spectral_norm            | 78.0 ms                                                     | 67.8 ms: 1.15x faster                                      |
| bench_thread_pool        | 946 us                                                      | 829 us: 1.14x faster                                       |
| docutils                 | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                     |
| deepcopy_memo            | 28.5 us                                                     | 25.1 us: 1.14x faster                                      |
| xml_etree_process        | 43.4 ms                                                     | 39.2 ms: 1.11x faster                                      |
| regex_compile            | 103 ms                                                      | 93.4 ms: 1.11x faster                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.09 sec: 1.10x faster                                     |
| pprint_safe_repr         | 589 ms                                                      | 533 ms: 1.10x faster                                       |
| regex_dna                | 132 ms                                                      | 120 ms: 1.10x faster                                       |
| unpickle                 | 9.17 us                                                     | 8.38 us: 1.10x faster                                      |
| python_startup           | 20.0 ms                                                     | 18.3 ms: 1.09x faster                                      |
| xml_etree_parse          | 102 ms                                                      | 93.8 ms: 1.08x faster                                      |
| dulwich_log              | 47.6 ms                                                     | 44.1 ms: 1.08x faster                                      |
| sqlglot_optimize         | 39.0 ms                                                     | 36.1 ms: 1.08x faster                                      |
| regex_v8                 | 15.0 ms                                                     | 14.0 ms: 1.08x faster                                      |
| json                     | 3.05 ms                                                     | 2.83 ms: 1.08x faster                                      |
| float                    | 60.2 ms                                                     | 56.1 ms: 1.07x faster                                      |
| create_gc_cycles         | 782 us                                                      | 730 us: 1.07x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                      |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 1.94 sec: 1.05x faster                                     |
| sqlite_synth             | 1.84 us                                                     | 1.76 us: 1.05x faster                                      |
| json_loads               | 14.2 us                                                     | 13.6 us: 1.04x faster                                      |
| nqueens                  | 67.0 ms                                                     | 64.3 ms: 1.04x faster                                      |
| sqlglot_normalize        | 202 ms                                                      | 194 ms: 1.04x faster                                       |
| coroutines               | 15.9 ms                                                     | 15.4 ms: 1.04x faster                                      |
| comprehensions           | 16.0 us                                                     | 15.5 us: 1.03x faster                                      |
| deepcopy                 | 255 us                                                      | 248 us: 1.03x faster                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.60 ms: 1.02x faster                                      |
| fannkuch                 | 258 ms                                                      | 254 ms: 1.01x faster                                       |
| unpickle_list            | 2.81 us                                                     | 2.77 us: 1.01x faster                                      |
| scimark_fft              | 193 ms                                                      | 196 ms: 1.01x slower                                       |
| pathlib                  | 77.4 ms                                                     | 79.4 ms: 1.03x slower                                      |
| pickle                   | 6.80 us                                                     | 6.98 us: 1.03x slower                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.21 us: 1.03x slower                                      |
| pidigits                 | 145 ms                                                      | 150 ms: 1.03x slower                                       |
| xml_etree_iterparse      | 63.5 ms                                                     | 65.6 ms: 1.03x slower                                      |
| meteor_contest           | 72.5 ms                                                     | 75.0 ms: 1.03x slower                                      |
| xml_etree_generate       | 54.5 ms                                                     | 56.8 ms: 1.04x slower                                      |
| pickle_list              | 2.59 us                                                     | 2.72 us: 1.05x slower                                      |
| pickle_dict              | 16.9 us                                                     | 18.0 us: 1.07x slower                                      |
| bench_mp_pool            | 60.7 ms                                                     | 66.3 ms: 1.09x slower                                      |
| logging_format           | 6.66 us                                                     | 7.33 us: 1.10x slower                                      |
| logging_simple           | 6.20 us                                                     | 6.84 us: 1.10x slower                                      |
| async_generators         | 224 ms                                                      | 247 ms: 1.10x slower                                       |
| nbody                    | 69.3 ms                                                     | 76.8 ms: 1.11x slower                                      |
| gc_traversal             | 1.34 ms                                                     | 1.49 ms: 1.11x slower                                      |
| unpack_sequence          | 37.8 ns                                                     | 42.2 ns: 1.11x slower                                      |
| telco                    | 3.78 ms                                                     | 4.39 ms: 1.16x slower                                      |
| dask                     | 305 ms                                                      | 382 ms: 1.25x slower                                       |
| coverage                 | 40.0 ms                                                     | 53.4 ms: 1.33x slower                                      |
| Geometric mean           | (ref)                                                       | 1.13x faster                                               |

Benchmark hidden because not significant (2): tomli_loads, python_startup_no_site
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
