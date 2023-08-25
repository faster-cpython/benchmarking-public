
# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 3.03 sec: 1.12x faster                                              |
| tornado_http   | 152 ms                                                       | 123 ms: 1.23x faster                                                |
| Geometric mean | (ref)                                                        | 1.18x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 94.7 ms: 1.45x faster                                               |
| float          | 110 ms                                                       | 85.3 ms: 1.29x faster                                               |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                        | 1.25x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 160 ms: 1.21x faster                                                |
| regex_v8       | 26.6 ms                                                      | 24.4 ms: 1.09x faster                                               |
| regex_dna      | 259 ms                                                       | 244 ms: 1.06x faster                                                |
| regex_effbot   | 2.99 ms                                                      | 3.55 ms: 1.19x slower                                               |
| Geometric mean | (ref)                                                        | 1.04x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 324 us: 1.41x faster                                                |
| unpickle_pure_python | 321 us                                                       | 237 us: 1.35x faster                                                |
| json_dumps           | 14.2 ms                                                      | 10.5 ms: 1.35x faster                                               |
| xml_etree_process    | 76.0 ms                                                      | 61.8 ms: 1.23x faster                                               |
| json_loads           | 30.0 us                                                      | 25.7 us: 1.17x faster                                               |
| tomli_loads          | 2.97 sec                                                     | 2.68 sec: 1.11x faster                                              |
| xml_etree_parse      | 162 ms                                                       | 149 ms: 1.09x faster                                                |
| xml_etree_generate   | 94.6 ms                                                      | 89.2 ms: 1.06x faster                                               |
| xml_etree_iterparse  | 110 ms                                                       | 109 ms: 1.02x faster                                                |
| pickle               | 9.94 us                                                      | 10.2 us: 1.03x slower                                               |
| unpickle             | 14.2 us                                                      | 14.7 us: 1.04x slower                                               |
| unpickle_list        | 4.49 us                                                      | 4.68 us: 1.04x slower                                               |
| pickle_dict          | 30.0 us                                                      | 32.3 us: 1.08x slower                                               |
| pickle_list          | 4.11 us                                                      | 4.45 us: 1.08x slower                                               |
| Geometric mean       | (ref)                                                        | 1.10x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                               |
| python_startup_no_site | 7.32 ms                                                      | 8.68 ms: 1.18x slower                                               |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 11.5 ms: 1.28x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 160 us: 3.26x faster                                                |
| asyncio_tcp              | 782 ms                                                       | 369 ms: 2.12x faster                                                |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                              |
| deltablue                | 7.47 ms                                                      | 3.89 ms: 1.92x faster                                               |
| raytrace                 | 488 ms                                                       | 294 ms: 1.66x faster                                                |
| logging_silent           | 166 ns                                                       | 100 ns: 1.65x faster                                                |
| chaos                    | 107 ms                                                       | 67.4 ms: 1.59x faster                                               |
| scimark_monte_carlo      | 109 ms                                                       | 70.6 ms: 1.55x faster                                               |
| bench_mp_pool            | 7.18 ms                                                      | 4.64 ms: 1.55x faster                                               |
| scimark_lu               | 164 ms                                                       | 106 ms: 1.54x faster                                                |
| generators               | 58.0 ms                                                      | 37.6 ms: 1.54x faster                                               |
| crypto_pyaes             | 118 ms                                                       | 77.6 ms: 1.52x faster                                               |
| sqlglot_parse            | 2.26 ms                                                      | 1.49 ms: 1.52x faster                                               |
| richards_super           | 90.8 ms                                                      | 60.2 ms: 1.51x faster                                               |
| async_tree_io            | 1.61 sec                                                     | 1.10 sec: 1.46x faster                                              |
| async_tree_none          | 700 ms                                                       | 481 ms: 1.45x faster                                                |
| nbody                    | 137 ms                                                       | 94.7 ms: 1.45x faster                                               |
| sqlglot_transpile        | 2.71 ms                                                      | 1.90 ms: 1.42x faster                                               |
| pickle_pure_python       | 457 us                                                       | 324 us: 1.41x faster                                                |
| async_tree_memoization   | 824 ms                                                       | 585 ms: 1.41x faster                                                |
| go                       | 259 ms                                                       | 186 ms: 1.39x faster                                                |
| unpickle_pure_python     | 321 us                                                       | 237 us: 1.35x faster                                                |
| json_dumps               | 14.2 ms                                                      | 10.5 ms: 1.35x faster                                               |
| richards                 | 74.1 ms                                                      | 55.0 ms: 1.35x faster                                               |
| spectral_norm            | 136 ms                                                       | 103 ms: 1.33x faster                                                |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 731 ms: 1.30x faster                                                |
| pyflate                  | 697 ms                                                       | 537 ms: 1.30x faster                                                |
| float                    | 110 ms                                                       | 85.3 ms: 1.29x faster                                               |
| mako                     | 14.7 ms                                                      | 11.5 ms: 1.28x faster                                               |
| coroutines               | 30.4 ms                                                      | 23.9 ms: 1.27x faster                                               |
| logging_simple           | 8.90 us                                                      | 7.04 us: 1.26x faster                                               |
| logging_format           | 9.57 us                                                      | 7.66 us: 1.25x faster                                               |
| tornado_http             | 152 ms                                                       | 123 ms: 1.23x faster                                                |
| xml_etree_process        | 76.0 ms                                                      | 61.8 ms: 1.23x faster                                               |
| pprint_safe_repr         | 1.05 sec                                                     | 861 ms: 1.22x faster                                                |
| pprint_pformat           | 2.15 sec                                                     | 1.77 sec: 1.22x faster                                              |
| pycparser                | 1.66 sec                                                     | 1.37 sec: 1.22x faster                                              |
| regex_compile            | 194 ms                                                       | 160 ms: 1.21x faster                                                |
| mypy2                    | 466 ms                                                       | 385 ms: 1.21x faster                                                |
| sqlglot_normalize        | 144 ms                                                       | 122 ms: 1.19x faster                                                |
| hexiom                   | 9.52 ms                                                      | 8.05 ms: 1.18x faster                                               |
| scimark_sor              | 177 ms                                                       | 150 ms: 1.18x faster                                                |
| deepcopy_memo            | 48.9 us                                                      | 41.6 us: 1.17x faster                                               |
| json_loads               | 30.0 us                                                      | 25.7 us: 1.17x faster                                               |
| deepcopy                 | 454 us                                                       | 392 us: 1.16x faster                                                |
| dulwich_log              | 80.1 ms                                                      | 69.4 ms: 1.15x faster                                               |
| deepcopy_reduce          | 4.03 us                                                      | 3.50 us: 1.15x faster                                               |
| json                     | 5.96 ms                                                      | 5.20 ms: 1.15x faster                                               |
| create_gc_cycles         | 1.82 ms                                                      | 1.59 ms: 1.15x faster                                               |
| bench_thread_pool        | 1.14 ms                                                      | 993 us: 1.14x faster                                                |
| sqlglot_optimize         | 70.3 ms                                                      | 61.8 ms: 1.14x faster                                               |
| docutils                 | 3.40 sec                                                     | 3.03 sec: 1.12x faster                                              |
| tomli_loads              | 2.97 sec                                                     | 2.68 sec: 1.11x faster                                              |
| mdp                      | 3.03 sec                                                     | 2.74 sec: 1.11x faster                                              |
| regex_v8                 | 26.6 ms                                                      | 24.4 ms: 1.09x faster                                               |
| xml_etree_parse          | 162 ms                                                       | 149 ms: 1.09x faster                                                |
| pathlib                  | 21.7 ms                                                      | 20.1 ms: 1.08x faster                                               |
| sqlite_synth             | 2.97 us                                                      | 2.78 us: 1.07x faster                                               |
| regex_dna                | 259 ms                                                       | 244 ms: 1.06x faster                                                |
| xml_etree_generate       | 94.6 ms                                                      | 89.2 ms: 1.06x faster                                               |
| scimark_fft              | 359 ms                                                       | 339 ms: 1.06x faster                                                |
| unpack_sequence          | 59.5 ns                                                      | 56.4 ns: 1.06x faster                                               |
| fannkuch                 | 496 ms                                                       | 471 ms: 1.05x faster                                                |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                                |
| nqueens                  | 112 ms                                                       | 109 ms: 1.03x faster                                                |
| async_generators         | 422 ms                                                       | 411 ms: 1.03x faster                                                |
| xml_etree_iterparse      | 110 ms                                                       | 109 ms: 1.02x faster                                                |
| comprehensions           | 26.9 us                                                      | 27.2 us: 1.01x slower                                               |
| python_startup           | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                               |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.03x slower                                               |
| unpickle                 | 14.2 us                                                      | 14.7 us: 1.04x slower                                               |
| unpickle_list            | 4.49 us                                                      | 4.68 us: 1.04x slower                                               |
| meteor_contest           | 137 ms                                                       | 143 ms: 1.05x slower                                                |
| pickle_dict              | 30.0 us                                                      | 32.3 us: 1.08x slower                                               |
| pickle_list              | 4.11 us                                                      | 4.45 us: 1.08x slower                                               |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 5.65 ms: 1.09x slower                                               |
| telco                    | 7.14 ms                                                      | 8.04 ms: 1.13x slower                                               |
| gc_traversal             | 3.45 ms                                                      | 3.95 ms: 1.14x slower                                               |
| python_startup_no_site   | 7.32 ms                                                      | 8.68 ms: 1.18x slower                                               |
| regex_effbot             | 2.99 ms                                                      | 3.55 ms: 1.19x slower                                               |
| dask                     | 463 ms                                                       | 597 ms: 1.29x slower                                                |
| coverage                 | 64.0 ms                                                      | 90.3 ms: 1.41x slower                                               |
| Geometric mean           | (ref)                                                        | 1.21x faster                                                        |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x
