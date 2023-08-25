
# Results vs. 3.10.4

- fork: brandtbucher
- ref: uops_enabled
- machine: windows-amd64
- commit hash: 9016d52
- commit date: 2023-08-06
- overall geometric mean: 1.07x faster
- HPT reliability: 99.72%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.76 sec: 1.08x faster                                                   |
| tornado_http   | 109 ms                                                      | 92.4 ms: 1.18x faster                                                    |
| Geometric mean | (ref)                                                       | 1.13x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 59.1 ms: 1.02x faster                                                    |
| pidigits       | 145 ms                                                      | 148 ms: 1.02x slower                                                     |
| nbody          | 69.3 ms                                                     | 82.6 ms: 1.19x slower                                                    |
| Geometric mean | (ref)                                                       | 1.06x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 132 ms                                                      | 122 ms: 1.09x faster                                                     |
| regex_v8       | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                                    |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.04x faster                                                    |
| regex_compile  | 103 ms                                                      | 101 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                       | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.87 ms: 1.45x faster                                                    |
| pickle_pure_python   | 257 us                                                      | 202 us: 1.27x faster                                                     |
| unpickle             | 9.17 us                                                     | 8.21 us: 1.12x faster                                                    |
| unpickle_pure_python | 171 us                                                      | 154 us: 1.11x faster                                                     |
| xml_etree_parse      | 102 ms                                                      | 93.2 ms: 1.09x faster                                                    |
| xml_etree_process    | 43.4 ms                                                     | 41.0 ms: 1.06x faster                                                    |
| json_loads           | 14.2 us                                                     | 13.7 us: 1.04x faster                                                    |
| unpickle_list        | 2.81 us                                                     | 2.93 us: 1.04x slower                                                    |
| xml_etree_iterparse  | 63.5 ms                                                     | 68.4 ms: 1.08x slower                                                    |
| tomli_loads          | 1.62 sec                                                    | 1.77 sec: 1.09x slower                                                   |
| pickle_dict          | 16.9 us                                                     | 18.5 us: 1.09x slower                                                    |
| pickle               | 6.80 us                                                     | 7.45 us: 1.09x slower                                                    |
| xml_etree_generate   | 54.5 ms                                                     | 59.9 ms: 1.10x slower                                                    |
| pickle_list          | 2.59 us                                                     | 2.87 us: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.0 ms: 1.05x faster                                                    |
| python_startup_no_site | 15.5 ms                                                     | 16.3 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                       | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|-----------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 8.28 ms: 1.06x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 102 us: 3.19x faster                                                     |
| deltablue                | 4.17 ms                                                     | 2.50 ms: 1.67x faster                                                    |
| mypy2                    | 352 ms                                                      | 230 ms: 1.53x faster                                                     |
| json_dumps               | 8.50 ms                                                     | 5.87 ms: 1.45x faster                                                    |
| richards_super           | 51.7 ms                                                     | 35.8 ms: 1.44x faster                                                    |
| logging_silent           | 96.4 ns                                                     | 67.5 ns: 1.43x faster                                                    |
| raytrace                 | 271 ms                                                      | 194 ms: 1.39x faster                                                     |
| asyncio_tcp              | 712 ms                                                      | 514 ms: 1.39x faster                                                     |
| async_tree_io            | 1.07 sec                                                    | 774 ms: 1.38x faster                                                     |
| async_tree_memoization   | 497 ms                                                      | 364 ms: 1.36x faster                                                     |
| sqlglot_parse            | 1.22 ms                                                     | 903 us: 1.35x faster                                                     |
| async_tree_none          | 420 ms                                                      | 312 ms: 1.35x faster                                                     |
| richards                 | 41.2 ms                                                     | 32.0 ms: 1.29x faster                                                    |
| go                       | 136 ms                                                      | 106 ms: 1.28x faster                                                     |
| sqlglot_transpile        | 1.46 ms                                                     | 1.14 ms: 1.28x faster                                                    |
| crypto_pyaes             | 62.3 ms                                                     | 49.0 ms: 1.27x faster                                                    |
| scimark_lu               | 85.4 ms                                                     | 67.3 ms: 1.27x faster                                                    |
| pickle_pure_python       | 257 us                                                      | 202 us: 1.27x faster                                                     |
| chaos                    | 58.9 ms                                                     | 47.8 ms: 1.23x faster                                                    |
| generators               | 31.6 ms                                                     | 25.7 ms: 1.23x faster                                                    |
| scimark_monte_carlo      | 55.9 ms                                                     | 45.6 ms: 1.22x faster                                                    |
| scimark_sor              | 105 ms                                                      | 87.6 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 514 ms: 1.18x faster                                                     |
| tornado_http             | 109 ms                                                      | 92.4 ms: 1.18x faster                                                    |
| pycparser                | 868 ms                                                      | 772 ms: 1.12x faster                                                     |
| unpickle                 | 9.17 us                                                     | 8.21 us: 1.12x faster                                                    |
| pyflate                  | 387 ms                                                      | 348 ms: 1.11x faster                                                     |
| unpickle_pure_python     | 171 us                                                      | 154 us: 1.11x faster                                                     |
| mdp                      | 1.71 sec                                                    | 1.57 sec: 1.09x faster                                                   |
| xml_etree_parse          | 102 ms                                                      | 93.2 ms: 1.09x faster                                                    |
| spectral_norm            | 78.0 ms                                                     | 71.7 ms: 1.09x faster                                                    |
| regex_dna                | 132 ms                                                      | 122 ms: 1.09x faster                                                     |
| regex_v8                 | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                                    |
| docutils                 | 1.89 sec                                                    | 1.76 sec: 1.08x faster                                                   |
| pprint_safe_repr         | 589 ms                                                      | 548 ms: 1.07x faster                                                     |
| pprint_pformat           | 1.21 sec                                                    | 1.13 sec: 1.07x faster                                                   |
| mako                     | 8.80 ms                                                     | 8.28 ms: 1.06x faster                                                    |
| xml_etree_process        | 43.4 ms                                                     | 41.0 ms: 1.06x faster                                                    |
| bench_thread_pool        | 946 us                                                      | 894 us: 1.06x faster                                                     |
| python_startup           | 20.0 ms                                                     | 19.0 ms: 1.05x faster                                                    |
| create_gc_cycles         | 782 us                                                      | 747 us: 1.05x faster                                                     |
| json                     | 3.05 ms                                                     | 2.92 ms: 1.05x faster                                                    |
| json_loads               | 14.2 us                                                     | 13.7 us: 1.04x faster                                                    |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.04x faster                                                    |
| sqlite_synth             | 1.84 us                                                     | 1.78 us: 1.03x faster                                                    |
| coroutines               | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                    |
| sqlglot_optimize         | 39.0 ms                                                     | 38.0 ms: 1.03x faster                                                    |
| regex_compile            | 103 ms                                                      | 101 ms: 1.03x faster                                                     |
| float                    | 60.2 ms                                                     | 59.1 ms: 1.02x faster                                                    |
| sqlglot_normalize        | 202 ms                                                      | 200 ms: 1.01x faster                                                     |
| hexiom                   | 5.52 ms                                                     | 5.48 ms: 1.01x faster                                                    |
| deepcopy_memo            | 28.5 us                                                     | 28.7 us: 1.01x slower                                                    |
| dulwich_log              | 47.6 ms                                                     | 48.2 ms: 1.01x slower                                                    |
| pidigits                 | 145 ms                                                      | 148 ms: 1.02x slower                                                     |
| deepcopy                 | 255 us                                                      | 262 us: 1.03x slower                                                     |
| unpickle_list            | 2.81 us                                                     | 2.93 us: 1.04x slower                                                    |
| python_startup_no_site   | 15.5 ms                                                     | 16.3 ms: 1.05x slower                                                    |
| unpack_sequence          | 37.8 ns                                                     | 39.9 ns: 1.05x slower                                                    |
| deepcopy_reduce          | 2.16 us                                                     | 2.28 us: 1.06x slower                                                    |
| scimark_fft              | 193 ms                                                      | 205 ms: 1.06x slower                                                     |
| xml_etree_iterparse      | 63.5 ms                                                     | 68.4 ms: 1.08x slower                                                    |
| tomli_loads              | 1.62 sec                                                    | 1.77 sec: 1.09x slower                                                   |
| pickle_dict              | 16.9 us                                                     | 18.5 us: 1.09x slower                                                    |
| pickle                   | 6.80 us                                                     | 7.45 us: 1.09x slower                                                    |
| xml_etree_generate       | 54.5 ms                                                     | 59.9 ms: 1.10x slower                                                    |
| pathlib                  | 77.4 ms                                                     | 85.1 ms: 1.10x slower                                                    |
| pickle_list              | 2.59 us                                                     | 2.87 us: 1.11x slower                                                    |
| nqueens                  | 67.0 ms                                                     | 74.6 ms: 1.11x slower                                                    |
| bench_mp_pool            | 60.7 ms                                                     | 68.0 ms: 1.12x slower                                                    |
| async_generators         | 224 ms                                                      | 254 ms: 1.14x slower                                                     |
| comprehensions           | 16.0 us                                                     | 18.2 us: 1.14x slower                                                    |
| gc_traversal             | 1.34 ms                                                     | 1.55 ms: 1.15x slower                                                    |
| meteor_contest           | 72.5 ms                                                     | 83.8 ms: 1.16x slower                                                    |
| fannkuch                 | 258 ms                                                      | 304 ms: 1.18x slower                                                     |
| logging_format           | 6.66 us                                                     | 7.89 us: 1.18x slower                                                    |
| logging_simple           | 6.20 us                                                     | 7.37 us: 1.19x slower                                                    |
| nbody                    | 69.3 ms                                                     | 82.6 ms: 1.19x slower                                                    |
| telco                    | 3.78 ms                                                     | 4.89 ms: 1.29x slower                                                    |
| dask                     | 305 ms                                                      | 397 ms: 1.30x slower                                                     |
| coverage                 | 40.0 ms                                                     | 52.9 ms: 1.32x slower                                                    |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 3.68 ms: 1.38x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.07x faster                                                             |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.72% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x
