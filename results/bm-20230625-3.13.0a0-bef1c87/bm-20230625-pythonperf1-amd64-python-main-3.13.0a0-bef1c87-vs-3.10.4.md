
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: bef1c87
- commit date: 2023-06-25
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-pythonperf1-amd64-python-main-3.13.0a0-bef1c87 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.65 sec: 1.15x faster                                     |
| tornado_http   | 109 ms                                                      | 91.1 ms: 1.20x faster                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-pythonperf1-amd64-python-main-3.13.0a0-bef1c87 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 55.5 ms: 1.08x faster                                      |
| pidigits       | 145 ms                                                      | 154 ms: 1.06x slower                                       |
| nbody          | 69.3 ms                                                     | 75.0 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-pythonperf1-amd64-python-main-3.13.0a0-bef1c87 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 87.3 ms: 1.18x faster                                      |
| regex_v8       | 15.0 ms                                                     | 13.7 ms: 1.10x faster                                      |
| regex_dna      | 132 ms                                                      | 120 ms: 1.10x faster                                       |
| regex_effbot   | 1.66 ms                                                     | 1.77 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-pythonperf1-amd64-python-main-3.13.0a0-bef1c87 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 6.07 ms: 1.40x faster                                      |
| pickle_pure_python   | 257 us                                                      | 197 us: 1.30x faster                                       |
| unpickle_pure_python | 171 us                                                      | 136 us: 1.26x faster                                       |
| xml_etree_process    | 43.4 ms                                                     | 38.6 ms: 1.13x faster                                      |
| tomli_loads          | 1.62 sec                                                    | 1.46 sec: 1.11x faster                                     |
| xml_etree_parse      | 102 ms                                                      | 93.4 ms: 1.09x faster                                      |
| unpickle             | 9.17 us                                                     | 8.61 us: 1.07x faster                                      |
| json_loads           | 14.2 us                                                     | 14.4 us: 1.02x slower                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 64.9 ms: 1.02x slower                                      |
| xml_etree_generate   | 54.5 ms                                                     | 55.8 ms: 1.02x slower                                      |
| unpickle_list        | 2.81 us                                                     | 2.89 us: 1.03x slower                                      |
| pickle               | 6.80 us                                                     | 7.14 us: 1.05x slower                                      |
| pickle_list          | 2.59 us                                                     | 2.76 us: 1.07x slower                                      |
| pickle_dict          | 16.9 us                                                     | 18.8 us: 1.11x slower                                      |
| Geometric mean       | (ref)                                                       | 1.07x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-pythonperf1-amd64-python-main-3.13.0a0-bef1c87 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 20.3 ms: 1.01x slower                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-pythonperf1-amd64-python-main-3.13.0a0-bef1c87 |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.43 ms: 1.19x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-pythonperf1-amd64-python-main-3.13.0a0-bef1c87 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 93.7 us: 3.47x faster                                      |
| deltablue                | 4.17 ms                                                     | 2.12 ms: 1.96x faster                                      |
| richards_super           | 51.7 ms                                                     | 29.7 ms: 1.74x faster                                      |
| mypy2                    | 352 ms                                                      | 219 ms: 1.60x faster                                       |
| raytrace                 | 271 ms                                                      | 170 ms: 1.60x faster                                       |
| richards                 | 41.2 ms                                                     | 26.0 ms: 1.58x faster                                      |
| logging_silent           | 96.4 ns                                                     | 61.3 ns: 1.57x faster                                      |
| sqlglot_parse            | 1.22 ms                                                     | 828 us: 1.47x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 341 ms: 1.46x faster                                       |
| chaos                    | 58.9 ms                                                     | 40.4 ms: 1.46x faster                                      |
| asyncio_tcp              | 712 ms                                                      | 490 ms: 1.46x faster                                       |
| go                       | 136 ms                                                      | 93.6 ms: 1.45x faster                                      |
| async_tree_io            | 1.07 sec                                                    | 741 ms: 1.44x faster                                       |
| scimark_lu               | 85.4 ms                                                     | 60.1 ms: 1.42x faster                                      |
| async_tree_none          | 420 ms                                                      | 297 ms: 1.42x faster                                       |
| sqlglot_transpile        | 1.46 ms                                                     | 1.04 ms: 1.41x faster                                      |
| json_dumps               | 8.50 ms                                                     | 6.07 ms: 1.40x faster                                      |
| generators               | 31.6 ms                                                     | 22.9 ms: 1.38x faster                                      |
| hexiom                   | 5.52 ms                                                     | 4.09 ms: 1.35x faster                                      |
| pickle_pure_python       | 257 us                                                      | 197 us: 1.30x faster                                       |
| crypto_pyaes             | 62.3 ms                                                     | 48.4 ms: 1.29x faster                                      |
| scimark_sor              | 105 ms                                                      | 82.7 ms: 1.27x faster                                      |
| unpickle_pure_python     | 171 us                                                      | 136 us: 1.26x faster                                       |
| pyflate                  | 387 ms                                                      | 310 ms: 1.25x faster                                       |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 493 ms: 1.24x faster                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 45.6 ms: 1.22x faster                                      |
| tornado_http             | 109 ms                                                      | 91.1 ms: 1.20x faster                                      |
| pycparser                | 868 ms                                                      | 726 ms: 1.19x faster                                       |
| mako                     | 8.80 ms                                                     | 7.43 ms: 1.19x faster                                      |
| regex_compile            | 103 ms                                                      | 87.3 ms: 1.18x faster                                      |
| deepcopy_memo            | 28.5 us                                                     | 24.2 us: 1.18x faster                                      |
| mdp                      | 1.71 sec                                                    | 1.46 sec: 1.17x faster                                     |
| docutils                 | 1.89 sec                                                    | 1.65 sec: 1.15x faster                                     |
| pprint_pformat           | 1.21 sec                                                    | 1.07 sec: 1.13x faster                                     |
| sqlglot_optimize         | 39.0 ms                                                     | 34.6 ms: 1.13x faster                                      |
| pprint_safe_repr         | 589 ms                                                      | 523 ms: 1.13x faster                                       |
| xml_etree_process        | 43.4 ms                                                     | 38.6 ms: 1.13x faster                                      |
| comprehensions           | 16.0 us                                                     | 14.3 us: 1.12x faster                                      |
| tomli_loads              | 1.62 sec                                                    | 1.46 sec: 1.11x faster                                     |
| nqueens                  | 67.0 ms                                                     | 60.3 ms: 1.11x faster                                      |
| spectral_norm            | 78.0 ms                                                     | 70.2 ms: 1.11x faster                                      |
| regex_v8                 | 15.0 ms                                                     | 13.7 ms: 1.10x faster                                      |
| regex_dna                | 132 ms                                                      | 120 ms: 1.10x faster                                       |
| sqlglot_normalize        | 202 ms                                                      | 185 ms: 1.09x faster                                       |
| xml_etree_parse          | 102 ms                                                      | 93.4 ms: 1.09x faster                                      |
| bench_thread_pool        | 946 us                                                      | 870 us: 1.09x faster                                       |
| float                    | 60.2 ms                                                     | 55.5 ms: 1.08x faster                                      |
| unpickle                 | 9.17 us                                                     | 8.61 us: 1.07x faster                                      |
| deepcopy                 | 255 us                                                      | 240 us: 1.06x faster                                       |
| sqlite_synth             | 1.84 us                                                     | 1.74 us: 1.06x faster                                      |
| coroutines               | 15.9 ms                                                     | 15.1 ms: 1.05x faster                                      |
| create_gc_cycles         | 782 us                                                      | 748 us: 1.05x faster                                       |
| deepcopy_reduce          | 2.16 us                                                     | 2.10 us: 1.03x faster                                      |
| dulwich_log              | 47.6 ms                                                     | 46.3 ms: 1.03x faster                                      |
| fannkuch                 | 258 ms                                                      | 251 ms: 1.03x faster                                       |
| scimark_fft              | 193 ms                                                      | 189 ms: 1.02x faster                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.62 ms: 1.01x faster                                      |
| python_startup           | 20.0 ms                                                     | 20.3 ms: 1.01x slower                                      |
| unpack_sequence          | 37.8 ns                                                     | 38.5 ns: 1.02x slower                                      |
| json_loads               | 14.2 us                                                     | 14.4 us: 1.02x slower                                      |
| xml_etree_iterparse      | 63.5 ms                                                     | 64.9 ms: 1.02x slower                                      |
| xml_etree_generate       | 54.5 ms                                                     | 55.8 ms: 1.02x slower                                      |
| unpickle_list            | 2.81 us                                                     | 2.89 us: 1.03x slower                                      |
| meteor_contest           | 72.5 ms                                                     | 74.7 ms: 1.03x slower                                      |
| logging_format           | 6.66 us                                                     | 6.95 us: 1.04x slower                                      |
| logging_simple           | 6.20 us                                                     | 6.49 us: 1.05x slower                                      |
| pickle                   | 6.80 us                                                     | 7.14 us: 1.05x slower                                      |
| pidigits                 | 145 ms                                                      | 154 ms: 1.06x slower                                       |
| telco                    | 3.78 ms                                                     | 4.01 ms: 1.06x slower                                      |
| regex_effbot             | 1.66 ms                                                     | 1.77 ms: 1.07x slower                                      |
| pickle_list              | 2.59 us                                                     | 2.76 us: 1.07x slower                                      |
| pathlib                  | 77.4 ms                                                     | 83.3 ms: 1.08x slower                                      |
| async_generators         | 224 ms                                                      | 242 ms: 1.08x slower                                       |
| nbody                    | 69.3 ms                                                     | 75.0 ms: 1.08x slower                                      |
| pickle_dict              | 16.9 us                                                     | 18.8 us: 1.11x slower                                      |
| bench_mp_pool            | 60.7 ms                                                     | 67.9 ms: 1.12x slower                                      |
| gc_traversal             | 1.34 ms                                                     | 1.53 ms: 1.13x slower                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                      |
| coverage                 | 40.0 ms                                                     | 52.2 ms: 1.30x slower                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                               |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, json
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x
