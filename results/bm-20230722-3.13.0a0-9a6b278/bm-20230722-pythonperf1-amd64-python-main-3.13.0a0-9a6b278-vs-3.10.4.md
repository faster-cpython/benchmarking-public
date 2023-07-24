
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 9a6b278
- commit date: 2023-07-22
- overall geometric mean: 1.14x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                     |
| tornado_http   | 109 ms                                                      | 88.8 ms: 1.23x faster                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 56.1 ms: 1.07x faster                                      |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                       |
| nbody          | 69.3 ms                                                     | 77.9 ms: 1.12x slower                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 93.1 ms: 1.11x faster                                      |
| regex_dna      | 132 ms                                                      | 119 ms: 1.11x faster                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.75 ms: 1.48x faster                                      |
| pickle_pure_python   | 257 us                                                      | 199 us: 1.29x faster                                       |
| unpickle_pure_python | 171 us                                                      | 143 us: 1.20x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 91.5 ms: 1.11x faster                                      |
| xml_etree_process    | 43.4 ms                                                     | 39.1 ms: 1.11x faster                                      |
| unpickle             | 9.17 us                                                     | 8.28 us: 1.11x faster                                      |
| json_loads           | 14.2 us                                                     | 13.6 us: 1.04x faster                                      |
| unpickle_list        | 2.81 us                                                     | 2.77 us: 1.01x faster                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 64.2 ms: 1.01x slower                                      |
| xml_etree_generate   | 54.5 ms                                                     | 56.6 ms: 1.04x slower                                      |
| pickle               | 6.80 us                                                     | 7.07 us: 1.04x slower                                      |
| pickle_list          | 2.59 us                                                     | 2.78 us: 1.07x slower                                      |
| pickle_dict          | 16.9 us                                                     | 18.5 us: 1.09x slower                                      |
| Geometric mean       | (ref)                                                       | 1.07x faster                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.6 ms: 1.08x faster                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278 |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.62 ms: 1.16x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 95.2 us: 3.41x faster                                      |
| deltablue                | 4.17 ms                                                     | 2.29 ms: 1.82x faster                                      |
| mypy2                    | 352 ms                                                      | 221 ms: 1.59x faster                                       |
| richards_super           | 51.7 ms                                                     | 34.7 ms: 1.49x faster                                      |
| asyncio_tcp              | 712 ms                                                      | 479 ms: 1.49x faster                                       |
| json_dumps               | 8.50 ms                                                     | 5.75 ms: 1.48x faster                                      |
| logging_silent           | 96.4 ns                                                     | 65.4 ns: 1.47x faster                                      |
| raytrace                 | 271 ms                                                      | 187 ms: 1.45x faster                                       |
| async_tree_io            | 1.07 sec                                                    | 740 ms: 1.44x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 852 us: 1.43x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 349 ms: 1.42x faster                                       |
| async_tree_none          | 420 ms                                                      | 297 ms: 1.41x faster                                       |
| go                       | 136 ms                                                      | 98.4 ms: 1.38x faster                                      |
| chaos                    | 58.9 ms                                                     | 43.3 ms: 1.36x faster                                      |
| sqlglot_transpile        | 1.46 ms                                                     | 1.08 ms: 1.36x faster                                      |
| scimark_lu               | 85.4 ms                                                     | 62.9 ms: 1.36x faster                                      |
| richards                 | 41.2 ms                                                     | 30.7 ms: 1.34x faster                                      |
| crypto_pyaes             | 62.3 ms                                                     | 46.8 ms: 1.33x faster                                      |
| generators               | 31.6 ms                                                     | 24.2 ms: 1.30x faster                                      |
| pickle_pure_python       | 257 us                                                      | 199 us: 1.29x faster                                       |
| scimark_sor              | 105 ms                                                      | 82.4 ms: 1.27x faster                                      |
| scimark_monte_carlo      | 55.9 ms                                                     | 44.6 ms: 1.25x faster                                      |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 487 ms: 1.25x faster                                       |
| hexiom                   | 5.52 ms                                                     | 4.43 ms: 1.25x faster                                      |
| tornado_http             | 109 ms                                                      | 88.8 ms: 1.23x faster                                      |
| pyflate                  | 387 ms                                                      | 320 ms: 1.21x faster                                       |
| unpickle_pure_python     | 171 us                                                      | 143 us: 1.20x faster                                       |
| mdp                      | 1.71 sec                                                    | 1.45 sec: 1.18x faster                                     |
| pycparser                | 868 ms                                                      | 735 ms: 1.18x faster                                       |
| mako                     | 8.80 ms                                                     | 7.62 ms: 1.16x faster                                      |
| spectral_norm            | 78.0 ms                                                     | 68.0 ms: 1.15x faster                                      |
| bench_thread_pool        | 946 us                                                      | 831 us: 1.14x faster                                       |
| docutils                 | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                     |
| deepcopy_memo            | 28.5 us                                                     | 25.2 us: 1.13x faster                                      |
| xml_etree_parse          | 102 ms                                                      | 91.5 ms: 1.11x faster                                      |
| xml_etree_process        | 43.4 ms                                                     | 39.1 ms: 1.11x faster                                      |
| regex_compile            | 103 ms                                                      | 93.1 ms: 1.11x faster                                      |
| unpickle                 | 9.17 us                                                     | 8.28 us: 1.11x faster                                      |
| regex_dna                | 132 ms                                                      | 119 ms: 1.11x faster                                       |
| pprint_pformat           | 1.21 sec                                                    | 1.09 sec: 1.11x faster                                     |
| pprint_safe_repr         | 589 ms                                                      | 533 ms: 1.10x faster                                       |
| sqlglot_optimize         | 39.0 ms                                                     | 35.7 ms: 1.09x faster                                      |
| create_gc_cycles         | 782 us                                                      | 721 us: 1.08x faster                                       |
| python_startup           | 20.0 ms                                                     | 18.6 ms: 1.08x faster                                      |
| nqueens                  | 67.0 ms                                                     | 62.4 ms: 1.07x faster                                      |
| float                    | 60.2 ms                                                     | 56.1 ms: 1.07x faster                                      |
| dulwich_log              | 47.6 ms                                                     | 44.5 ms: 1.07x faster                                      |
| comprehensions           | 16.0 us                                                     | 15.0 us: 1.07x faster                                      |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                      |
| sqlglot_normalize        | 202 ms                                                      | 191 ms: 1.06x faster                                       |
| sqlite_synth             | 1.84 us                                                     | 1.74 us: 1.06x faster                                      |
| coroutines               | 15.9 ms                                                     | 15.1 ms: 1.05x faster                                      |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.52 ms: 1.05x faster                                      |
| json                     | 3.05 ms                                                     | 2.91 ms: 1.05x faster                                      |
| json_loads               | 14.2 us                                                     | 13.6 us: 1.04x faster                                      |
| scimark_fft              | 193 ms                                                      | 185 ms: 1.04x faster                                       |
| deepcopy                 | 255 us                                                      | 246 us: 1.04x faster                                       |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 1.97 sec: 1.03x faster                                     |
| unpickle_list            | 2.81 us                                                     | 2.77 us: 1.01x faster                                      |
| xml_etree_iterparse      | 63.5 ms                                                     | 64.2 ms: 1.01x slower                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.20 us: 1.02x slower                                      |
| meteor_contest           | 72.5 ms                                                     | 74.7 ms: 1.03x slower                                      |
| pidigits                 | 145 ms                                                      | 150 ms: 1.03x slower                                       |
| pathlib                  | 77.4 ms                                                     | 80.2 ms: 1.04x slower                                      |
| xml_etree_generate       | 54.5 ms                                                     | 56.6 ms: 1.04x slower                                      |
| pickle                   | 6.80 us                                                     | 7.07 us: 1.04x slower                                      |
| unpack_sequence          | 37.8 ns                                                     | 39.6 ns: 1.05x slower                                      |
| async_generators         | 224 ms                                                      | 240 ms: 1.07x slower                                       |
| pickle_list              | 2.59 us                                                     | 2.78 us: 1.07x slower                                      |
| pickle_dict              | 16.9 us                                                     | 18.5 us: 1.09x slower                                      |
| bench_mp_pool            | 60.7 ms                                                     | 66.6 ms: 1.10x slower                                      |
| logging_format           | 6.66 us                                                     | 7.36 us: 1.10x slower                                      |
| logging_simple           | 6.20 us                                                     | 6.88 us: 1.11x slower                                      |
| gc_traversal             | 1.34 ms                                                     | 1.50 ms: 1.11x slower                                      |
| nbody                    | 69.3 ms                                                     | 77.9 ms: 1.12x slower                                      |
| telco                    | 3.78 ms                                                     | 4.53 ms: 1.20x slower                                      |
| dask                     | 305 ms                                                      | 381 ms: 1.25x slower                                       |
| coverage                 | 40.0 ms                                                     | 53.7 ms: 1.34x slower                                      |
| Geometric mean           | (ref)                                                       | 1.14x faster                                               |

Benchmark hidden because not significant (4): regex_v8, tomli_loads, fannkuch, python_startup_no_site
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
