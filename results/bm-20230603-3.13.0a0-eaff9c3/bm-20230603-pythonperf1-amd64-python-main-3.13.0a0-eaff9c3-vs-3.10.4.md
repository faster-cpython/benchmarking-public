
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: eaff9c3
- commit date: 2023-06-03
- overall geometric mean: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                     |
| tornado_http   | 109 ms                                                      | 90.7 ms: 1.20x faster                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 54.1 ms: 1.11x faster                                      |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 87.5 ms: 1.18x faster                                      |
| regex_dna      | 132 ms                                                      | 127 ms: 1.03x faster                                       |
| regex_effbot   | 1.66 ms                                                     | 1.70 ms: 1.02x slower                                      |
| regex_v8       | 15.0 ms                                                     | 24.5 ms: 1.63x slower                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.84 ms: 1.46x faster                                      |
| pickle_pure_python   | 257 us                                                      | 191 us: 1.34x faster                                       |
| unpickle_pure_python | 171 us                                                      | 134 us: 1.28x faster                                       |
| tomli_loads          | 1.62 sec                                                    | 1.37 sec: 1.19x faster                                     |
| xml_etree_process    | 43.4 ms                                                     | 37.7 ms: 1.15x faster                                      |
| unpickle             | 9.17 us                                                     | 8.29 us: 1.11x faster                                      |
| xml_etree_parse      | 102 ms                                                      | 94.0 ms: 1.08x faster                                      |
| json_loads           | 14.2 us                                                     | 13.7 us: 1.03x faster                                      |
| xml_etree_generate   | 54.5 ms                                                     | 54.9 ms: 1.01x slower                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.0 ms: 1.02x slower                                      |
| unpickle_list        | 2.81 us                                                     | 2.88 us: 1.02x slower                                      |
| pickle               | 6.80 us                                                     | 7.28 us: 1.07x slower                                      |
| pickle_list          | 2.59 us                                                     | 2.86 us: 1.11x slower                                      |
| pickle_dict          | 16.9 us                                                     | 18.8 us: 1.11x slower                                      |
| Geometric mean       | (ref)                                                       | 1.08x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.2 ms: 1.04x faster                                      |
| python_startup_no_site | 15.5 ms                                                     | 16.2 ms: 1.04x slower                                      |
| Geometric mean         | (ref)                                                       | 1.00x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3 |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.69 ms: 1.31x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 95.1 us: 3.41x faster                                      |
| deltablue                | 4.17 ms                                                     | 2.12 ms: 1.97x faster                                      |
| richards_super           | 51.7 ms                                                     | 29.2 ms: 1.77x faster                                      |
| mypy2                    | 352 ms                                                      | 216 ms: 1.63x faster                                       |
| logging_silent           | 96.4 ns                                                     | 59.9 ns: 1.61x faster                                      |
| richards                 | 41.2 ms                                                     | 25.6 ms: 1.61x faster                                      |
| go                       | 136 ms                                                      | 88.3 ms: 1.54x faster                                      |
| sqlglot_parse            | 1.22 ms                                                     | 813 us: 1.50x faster                                       |
| scimark_lu               | 85.4 ms                                                     | 57.7 ms: 1.48x faster                                      |
| generators               | 31.6 ms                                                     | 21.4 ms: 1.48x faster                                      |
| async_tree_io            | 1.07 sec                                                    | 731 ms: 1.46x faster                                       |
| json_dumps               | 8.50 ms                                                     | 5.84 ms: 1.46x faster                                      |
| async_tree_none          | 420 ms                                                      | 289 ms: 1.45x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 343 ms: 1.45x faster                                       |
| raytrace                 | 271 ms                                                      | 189 ms: 1.43x faster                                       |
| sqlglot_transpile        | 1.46 ms                                                     | 1.03 ms: 1.42x faster                                      |
| chaos                    | 58.9 ms                                                     | 42.8 ms: 1.38x faster                                      |
| hexiom                   | 5.52 ms                                                     | 4.03 ms: 1.37x faster                                      |
| pyflate                  | 387 ms                                                      | 287 ms: 1.35x faster                                       |
| pickle_pure_python       | 257 us                                                      | 191 us: 1.34x faster                                       |
| mako                     | 8.80 ms                                                     | 6.69 ms: 1.31x faster                                      |
| crypto_pyaes             | 62.3 ms                                                     | 48.0 ms: 1.30x faster                                      |
| scimark_sor              | 105 ms                                                      | 81.1 ms: 1.29x faster                                      |
| scimark_monte_carlo      | 55.9 ms                                                     | 43.3 ms: 1.29x faster                                      |
| unpickle_pure_python     | 171 us                                                      | 134 us: 1.28x faster                                       |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 486 ms: 1.25x faster                                       |
| pycparser                | 868 ms                                                      | 700 ms: 1.24x faster                                       |
| spectral_norm            | 78.0 ms                                                     | 63.2 ms: 1.24x faster                                      |
| asyncio_tcp              | 712 ms                                                      | 592 ms: 1.20x faster                                       |
| tornado_http             | 109 ms                                                      | 90.7 ms: 1.20x faster                                      |
| tomli_loads              | 1.62 sec                                                    | 1.37 sec: 1.19x faster                                     |
| regex_compile            | 103 ms                                                      | 87.5 ms: 1.18x faster                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.03 sec: 1.17x faster                                     |
| deepcopy_memo            | 28.5 us                                                     | 24.6 us: 1.16x faster                                      |
| pprint_safe_repr         | 589 ms                                                      | 509 ms: 1.16x faster                                       |
| xml_etree_process        | 43.4 ms                                                     | 37.7 ms: 1.15x faster                                      |
| sqlglot_optimize         | 39.0 ms                                                     | 33.9 ms: 1.15x faster                                      |
| docutils                 | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                     |
| coroutines               | 15.9 ms                                                     | 14.1 ms: 1.13x faster                                      |
| mdp                      | 1.71 sec                                                    | 1.51 sec: 1.13x faster                                     |
| float                    | 60.2 ms                                                     | 54.1 ms: 1.11x faster                                      |
| bench_thread_pool        | 946 us                                                      | 851 us: 1.11x faster                                       |
| nqueens                  | 67.0 ms                                                     | 60.4 ms: 1.11x faster                                      |
| unpickle                 | 9.17 us                                                     | 8.29 us: 1.11x faster                                      |
| create_gc_cycles         | 782 us                                                      | 711 us: 1.10x faster                                       |
| sqlglot_normalize        | 202 ms                                                      | 185 ms: 1.09x faster                                       |
| xml_etree_parse          | 102 ms                                                      | 94.0 ms: 1.08x faster                                      |
| fannkuch                 | 258 ms                                                      | 240 ms: 1.07x faster                                       |
| deepcopy                 | 255 us                                                      | 238 us: 1.07x faster                                       |
| comprehensions           | 16.0 us                                                     | 14.9 us: 1.07x faster                                      |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.50 ms: 1.06x faster                                      |
| dulwich_log              | 47.6 ms                                                     | 45.0 ms: 1.06x faster                                      |
| sqlite_synth             | 1.84 us                                                     | 1.74 us: 1.06x faster                                      |
| json                     | 3.05 ms                                                     | 2.90 ms: 1.05x faster                                      |
| scimark_fft              | 193 ms                                                      | 184 ms: 1.05x faster                                       |
| python_startup           | 20.0 ms                                                     | 19.2 ms: 1.04x faster                                      |
| regex_dna                | 132 ms                                                      | 127 ms: 1.03x faster                                       |
| json_loads               | 14.2 us                                                     | 13.7 us: 1.03x faster                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.11 us: 1.02x faster                                      |
| xml_etree_generate       | 54.5 ms                                                     | 54.9 ms: 1.01x slower                                      |
| xml_etree_iterparse      | 63.5 ms                                                     | 65.0 ms: 1.02x slower                                      |
| regex_effbot             | 1.66 ms                                                     | 1.70 ms: 1.02x slower                                      |
| unpickle_list            | 2.81 us                                                     | 2.88 us: 1.02x slower                                      |
| logging_simple           | 6.20 us                                                     | 6.37 us: 1.03x slower                                      |
| logging_format           | 6.66 us                                                     | 6.87 us: 1.03x slower                                      |
| unpack_sequence          | 37.8 ns                                                     | 39.1 ns: 1.03x slower                                      |
| pidigits                 | 145 ms                                                      | 151 ms: 1.04x slower                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.2 ms: 1.04x slower                                      |
| meteor_contest           | 72.5 ms                                                     | 76.1 ms: 1.05x slower                                      |
| pickle                   | 6.80 us                                                     | 7.28 us: 1.07x slower                                      |
| async_generators         | 224 ms                                                      | 241 ms: 1.08x slower                                       |
| telco                    | 3.78 ms                                                     | 4.07 ms: 1.08x slower                                      |
| gc_traversal             | 1.34 ms                                                     | 1.48 ms: 1.10x slower                                      |
| pickle_list              | 2.59 us                                                     | 2.86 us: 1.11x slower                                      |
| pickle_dict              | 16.9 us                                                     | 18.8 us: 1.11x slower                                      |
| pathlib                  | 77.4 ms                                                     | 87.2 ms: 1.13x slower                                      |
| bench_mp_pool            | 60.7 ms                                                     | 68.7 ms: 1.13x slower                                      |
| coverage                 | 40.0 ms                                                     | 52.0 ms: 1.30x slower                                      |
| regex_v8                 | 15.0 ms                                                     | 24.5 ms: 1.63x slower                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                               |

Benchmark hidden because not significant (2): nbody, asyncio_tcp_ssl
Ignored benchmarks (17) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
