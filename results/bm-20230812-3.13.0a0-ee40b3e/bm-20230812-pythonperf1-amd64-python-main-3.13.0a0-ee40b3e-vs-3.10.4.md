
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: ee40b3e
- commit date: 2023-08-12
- overall geometric mean: 1.13x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.65 sec: 1.15x faster                                     |
| tornado_http   | 109 ms                                                      | 89.0 ms: 1.23x faster                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 55.8 ms: 1.08x faster                                      |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                       |
| nbody          | 69.3 ms                                                     | 78.2 ms: 1.13x slower                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 93.8 ms: 1.10x faster                                      |
| regex_v8       | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                      |
| regex_dna      | 132 ms                                                      | 122 ms: 1.09x faster                                       |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.70 ms: 1.49x faster                                      |
| pickle_pure_python   | 257 us                                                      | 198 us: 1.30x faster                                       |
| unpickle_pure_python | 171 us                                                      | 145 us: 1.18x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 91.8 ms: 1.11x faster                                      |
| xml_etree_process    | 43.4 ms                                                     | 39.5 ms: 1.10x faster                                      |
| unpickle             | 9.17 us                                                     | 8.63 us: 1.06x faster                                      |
| tomli_loads          | 1.62 sec                                                    | 1.54 sec: 1.06x faster                                     |
| json_loads           | 14.2 us                                                     | 13.6 us: 1.05x faster                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.0 ms: 1.02x slower                                      |
| xml_etree_generate   | 54.5 ms                                                     | 56.4 ms: 1.04x slower                                      |
| pickle               | 6.80 us                                                     | 7.30 us: 1.07x slower                                      |
| pickle_dict          | 16.9 us                                                     | 18.3 us: 1.08x slower                                      |
| pickle_list          | 2.59 us                                                     | 2.87 us: 1.11x slower                                      |
| Geometric mean       | (ref)                                                       | 1.06x faster                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.6 ms: 1.02x faster                                      |
| python_startup_no_site | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                      |
| Geometric mean         | (ref)                                                       | 1.02x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.57 ms: 1.16x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 99.2 us: 3.27x faster                                      |
| deltablue                | 4.17 ms                                                     | 2.29 ms: 1.82x faster                                      |
| async_tree_none          | 420 ms                                                      | 278 ms: 1.51x faster                                       |
| asyncio_tcp              | 712 ms                                                      | 474 ms: 1.50x faster                                       |
| raytrace                 | 271 ms                                                      | 181 ms: 1.50x faster                                       |
| richards_super           | 51.7 ms                                                     | 34.6 ms: 1.49x faster                                      |
| json_dumps               | 8.50 ms                                                     | 5.70 ms: 1.49x faster                                      |
| logging_silent           | 96.4 ns                                                     | 64.7 ns: 1.49x faster                                      |
| async_tree_io            | 1.07 sec                                                    | 739 ms: 1.44x faster                                       |
| scimark_lu               | 85.4 ms                                                     | 59.4 ms: 1.44x faster                                      |
| sqlglot_parse            | 1.22 ms                                                     | 863 us: 1.41x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 356 ms: 1.40x faster                                       |
| go                       | 136 ms                                                      | 98.2 ms: 1.39x faster                                      |
| richards                 | 41.2 ms                                                     | 30.2 ms: 1.36x faster                                      |
| crypto_pyaes             | 62.3 ms                                                     | 46.0 ms: 1.36x faster                                      |
| sqlglot_transpile        | 1.46 ms                                                     | 1.09 ms: 1.35x faster                                      |
| chaos                    | 58.9 ms                                                     | 43.8 ms: 1.35x faster                                      |
| pickle_pure_python       | 257 us                                                      | 198 us: 1.30x faster                                       |
| generators               | 31.6 ms                                                     | 24.8 ms: 1.27x faster                                      |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 482 ms: 1.26x faster                                       |
| hexiom                   | 5.52 ms                                                     | 4.44 ms: 1.24x faster                                      |
| scimark_sor              | 105 ms                                                      | 84.9 ms: 1.24x faster                                      |
| pyflate                  | 387 ms                                                      | 315 ms: 1.23x faster                                       |
| tornado_http             | 109 ms                                                      | 89.0 ms: 1.23x faster                                      |
| scimark_monte_carlo      | 55.9 ms                                                     | 45.6 ms: 1.23x faster                                      |
| unpickle_pure_python     | 171 us                                                      | 145 us: 1.18x faster                                       |
| pycparser                | 868 ms                                                      | 743 ms: 1.17x faster                                       |
| mypy2                    | 352 ms                                                      | 302 ms: 1.17x faster                                       |
| mako                     | 8.80 ms                                                     | 7.57 ms: 1.16x faster                                      |
| docutils                 | 1.89 sec                                                    | 1.65 sec: 1.15x faster                                     |
| spectral_norm            | 78.0 ms                                                     | 68.0 ms: 1.15x faster                                      |
| mdp                      | 1.71 sec                                                    | 1.50 sec: 1.14x faster                                     |
| bench_thread_pool        | 946 us                                                      | 835 us: 1.13x faster                                       |
| deepcopy_memo            | 28.5 us                                                     | 25.4 us: 1.12x faster                                      |
| xml_etree_parse          | 102 ms                                                      | 91.8 ms: 1.11x faster                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.09 sec: 1.11x faster                                     |
| pprint_safe_repr         | 589 ms                                                      | 533 ms: 1.11x faster                                       |
| regex_compile            | 103 ms                                                      | 93.8 ms: 1.10x faster                                      |
| xml_etree_process        | 43.4 ms                                                     | 39.5 ms: 1.10x faster                                      |
| sqlglot_optimize         | 39.0 ms                                                     | 35.8 ms: 1.09x faster                                      |
| regex_v8                 | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                      |
| regex_dna                | 132 ms                                                      | 122 ms: 1.09x faster                                       |
| float                    | 60.2 ms                                                     | 55.8 ms: 1.08x faster                                      |
| create_gc_cycles         | 782 us                                                      | 729 us: 1.07x faster                                       |
| json                     | 3.05 ms                                                     | 2.85 ms: 1.07x faster                                      |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.49 ms: 1.07x faster                                      |
| comprehensions           | 16.0 us                                                     | 15.0 us: 1.07x faster                                      |
| unpickle                 | 9.17 us                                                     | 8.63 us: 1.06x faster                                      |
| scimark_fft              | 193 ms                                                      | 182 ms: 1.06x faster                                       |
| tomli_loads              | 1.62 sec                                                    | 1.54 sec: 1.06x faster                                     |
| sqlite_synth             | 1.84 us                                                     | 1.74 us: 1.06x faster                                      |
| sqlglot_normalize        | 202 ms                                                      | 193 ms: 1.05x faster                                       |
| nqueens                  | 67.0 ms                                                     | 64.0 ms: 1.05x faster                                      |
| dulwich_log              | 47.6 ms                                                     | 45.5 ms: 1.05x faster                                      |
| json_loads               | 14.2 us                                                     | 13.6 us: 1.05x faster                                      |
| coroutines               | 15.9 ms                                                     | 15.3 ms: 1.04x faster                                      |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 1.96 sec: 1.04x faster                                     |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.04x faster                                      |
| python_startup           | 20.0 ms                                                     | 19.6 ms: 1.02x faster                                      |
| pathlib                  | 77.4 ms                                                     | 78.5 ms: 1.01x slower                                      |
| meteor_contest           | 72.5 ms                                                     | 74.0 ms: 1.02x slower                                      |
| fannkuch                 | 258 ms                                                      | 264 ms: 1.02x slower                                       |
| xml_etree_iterparse      | 63.5 ms                                                     | 65.0 ms: 1.02x slower                                      |
| xml_etree_generate       | 54.5 ms                                                     | 56.4 ms: 1.04x slower                                      |
| pidigits                 | 145 ms                                                      | 151 ms: 1.04x slower                                       |
| deepcopy_reduce          | 2.16 us                                                     | 2.26 us: 1.05x slower                                      |
| python_startup_no_site   | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                      |
| pickle                   | 6.80 us                                                     | 7.30 us: 1.07x slower                                      |
| logging_simple           | 6.20 us                                                     | 6.66 us: 1.07x slower                                      |
| logging_format           | 6.66 us                                                     | 7.18 us: 1.08x slower                                      |
| pickle_dict              | 16.9 us                                                     | 18.3 us: 1.08x slower                                      |
| bench_mp_pool            | 60.7 ms                                                     | 66.1 ms: 1.09x slower                                      |
| async_generators         | 224 ms                                                      | 245 ms: 1.09x slower                                       |
| pickle_list              | 2.59 us                                                     | 2.87 us: 1.11x slower                                      |
| gc_traversal             | 1.34 ms                                                     | 1.50 ms: 1.11x slower                                      |
| unpack_sequence          | 37.8 ns                                                     | 42.6 ns: 1.13x slower                                      |
| nbody                    | 69.3 ms                                                     | 78.2 ms: 1.13x slower                                      |
| coverage                 | 40.0 ms                                                     | 45.9 ms: 1.15x slower                                      |
| telco                    | 3.78 ms                                                     | 4.74 ms: 1.25x slower                                      |
| dask                     | 305 ms                                                      | 383 ms: 1.26x slower                                       |
| Geometric mean           | (ref)                                                       | 1.13x faster                                               |

Benchmark hidden because not significant (2): deepcopy, unpickle_list
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
