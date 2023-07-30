
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 5113ed7
- commit date: 2023-07-29
- overall geometric mean: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf1-amd64-python-main-3.13.0a0-5113ed7 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.70 sec: 1.11x faster                                     |
| tornado_http   | 109 ms                                                      | 91.0 ms: 1.20x faster                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf1-amd64-python-main-3.13.0a0-5113ed7 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 55.9 ms: 1.08x faster                                      |
| pidigits       | 145 ms                                                      | 147 ms: 1.01x slower                                       |
| nbody          | 69.3 ms                                                     | 76.7 ms: 1.11x slower                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf1-amd64-python-main-3.13.0a0-5113ed7 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 15.0 ms                                                     | 13.6 ms: 1.11x faster                                      |
| regex_compile  | 103 ms                                                      | 94.2 ms: 1.10x faster                                      |
| regex_dna      | 132 ms                                                      | 122 ms: 1.08x faster                                       |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf1-amd64-python-main-3.13.0a0-5113ed7 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.77 ms: 1.47x faster                                      |
| pickle_pure_python   | 257 us                                                      | 198 us: 1.30x faster                                       |
| unpickle_pure_python | 171 us                                                      | 146 us: 1.17x faster                                       |
| xml_etree_process    | 43.4 ms                                                     | 39.2 ms: 1.11x faster                                      |
| unpickle             | 9.17 us                                                     | 8.38 us: 1.09x faster                                      |
| xml_etree_parse      | 102 ms                                                      | 93.5 ms: 1.09x faster                                      |
| json_loads           | 14.2 us                                                     | 13.9 us: 1.02x faster                                      |
| unpickle_list        | 2.81 us                                                     | 2.87 us: 1.02x slower                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.6 ms: 1.03x slower                                      |
| xml_etree_generate   | 54.5 ms                                                     | 57.4 ms: 1.05x slower                                      |
| pickle               | 6.80 us                                                     | 7.33 us: 1.08x slower                                      |
| pickle_list          | 2.59 us                                                     | 2.87 us: 1.11x slower                                      |
| pickle_dict          | 16.9 us                                                     | 18.9 us: 1.12x slower                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf1-amd64-python-main-3.13.0a0-5113ed7 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.4 ms: 1.03x faster                                      |
| python_startup_no_site | 15.5 ms                                                     | 16.6 ms: 1.07x slower                                      |
| Geometric mean         | (ref)                                                       | 1.02x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf1-amd64-python-main-3.13.0a0-5113ed7 |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.56 ms: 1.16x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf1-amd64-python-main-3.13.0a0-5113ed7 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 95.6 us: 3.40x faster                                      |
| deltablue                | 4.17 ms                                                     | 2.33 ms: 1.79x faster                                      |
| mypy2                    | 352 ms                                                      | 222 ms: 1.58x faster                                       |
| richards_super           | 51.7 ms                                                     | 34.3 ms: 1.51x faster                                      |
| logging_silent           | 96.4 ns                                                     | 65.2 ns: 1.48x faster                                      |
| json_dumps               | 8.50 ms                                                     | 5.77 ms: 1.47x faster                                      |
| raytrace                 | 271 ms                                                      | 187 ms: 1.45x faster                                       |
| asyncio_tcp              | 712 ms                                                      | 502 ms: 1.42x faster                                       |
| scimark_lu               | 85.4 ms                                                     | 60.8 ms: 1.40x faster                                      |
| async_tree_io            | 1.07 sec                                                    | 764 ms: 1.39x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 880 us: 1.38x faster                                       |
| go                       | 136 ms                                                      | 98.4 ms: 1.38x faster                                      |
| async_tree_memoization   | 497 ms                                                      | 363 ms: 1.37x faster                                       |
| async_tree_none          | 420 ms                                                      | 311 ms: 1.35x faster                                       |
| richards                 | 41.2 ms                                                     | 30.6 ms: 1.34x faster                                      |
| crypto_pyaes             | 62.3 ms                                                     | 46.5 ms: 1.34x faster                                      |
| chaos                    | 58.9 ms                                                     | 44.2 ms: 1.33x faster                                      |
| sqlglot_transpile        | 1.46 ms                                                     | 1.11 ms: 1.32x faster                                      |
| pickle_pure_python       | 257 us                                                      | 198 us: 1.30x faster                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 43.8 ms: 1.27x faster                                      |
| generators               | 31.6 ms                                                     | 25.2 ms: 1.25x faster                                      |
| hexiom                   | 5.52 ms                                                     | 4.47 ms: 1.23x faster                                      |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 499 ms: 1.22x faster                                       |
| scimark_sor              | 105 ms                                                      | 86.2 ms: 1.22x faster                                      |
| tornado_http             | 109 ms                                                      | 91.0 ms: 1.20x faster                                      |
| pyflate                  | 387 ms                                                      | 325 ms: 1.19x faster                                       |
| spectral_norm            | 78.0 ms                                                     | 66.2 ms: 1.18x faster                                      |
| unpickle_pure_python     | 171 us                                                      | 146 us: 1.17x faster                                       |
| mdp                      | 1.71 sec                                                    | 1.47 sec: 1.17x faster                                     |
| mako                     | 8.80 ms                                                     | 7.56 ms: 1.16x faster                                      |
| deepcopy_memo            | 28.5 us                                                     | 25.2 us: 1.13x faster                                      |
| bench_thread_pool        | 946 us                                                      | 839 us: 1.13x faster                                       |
| pycparser                | 868 ms                                                      | 775 ms: 1.12x faster                                       |
| docutils                 | 1.89 sec                                                    | 1.70 sec: 1.11x faster                                     |
| xml_etree_process        | 43.4 ms                                                     | 39.2 ms: 1.11x faster                                      |
| regex_v8                 | 15.0 ms                                                     | 13.6 ms: 1.11x faster                                      |
| regex_compile            | 103 ms                                                      | 94.2 ms: 1.10x faster                                      |
| unpickle                 | 9.17 us                                                     | 8.38 us: 1.09x faster                                      |
| xml_etree_parse          | 102 ms                                                      | 93.5 ms: 1.09x faster                                      |
| regex_dna                | 132 ms                                                      | 122 ms: 1.08x faster                                       |
| float                    | 60.2 ms                                                     | 55.9 ms: 1.08x faster                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.12 sec: 1.07x faster                                     |
| sqlglot_optimize         | 39.0 ms                                                     | 36.7 ms: 1.06x faster                                      |
| pprint_safe_repr         | 589 ms                                                      | 556 ms: 1.06x faster                                       |
| comprehensions           | 16.0 us                                                     | 15.2 us: 1.05x faster                                      |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.54 ms: 1.05x faster                                      |
| deepcopy                 | 255 us                                                      | 244 us: 1.05x faster                                       |
| coroutines               | 15.9 ms                                                     | 15.3 ms: 1.04x faster                                      |
| create_gc_cycles         | 782 us                                                      | 754 us: 1.04x faster                                       |
| json                     | 3.05 ms                                                     | 2.95 ms: 1.03x faster                                      |
| python_startup           | 20.0 ms                                                     | 19.4 ms: 1.03x faster                                      |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                      |
| nqueens                  | 67.0 ms                                                     | 65.2 ms: 1.03x faster                                      |
| sqlglot_normalize        | 202 ms                                                      | 198 ms: 1.02x faster                                       |
| sqlite_synth             | 1.84 us                                                     | 1.80 us: 1.02x faster                                      |
| json_loads               | 14.2 us                                                     | 13.9 us: 1.02x faster                                      |
| dulwich_log              | 47.6 ms                                                     | 47.0 ms: 1.01x faster                                      |
| unpack_sequence          | 37.8 ns                                                     | 38.3 ns: 1.01x slower                                      |
| pidigits                 | 145 ms                                                      | 147 ms: 1.01x slower                                       |
| fannkuch                 | 258 ms                                                      | 262 ms: 1.02x slower                                       |
| unpickle_list            | 2.81 us                                                     | 2.87 us: 1.02x slower                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.21 us: 1.03x slower                                      |
| xml_etree_iterparse      | 63.5 ms                                                     | 65.6 ms: 1.03x slower                                      |
| xml_etree_generate       | 54.5 ms                                                     | 57.4 ms: 1.05x slower                                      |
| meteor_contest           | 72.5 ms                                                     | 77.2 ms: 1.06x slower                                      |
| python_startup_no_site   | 15.5 ms                                                     | 16.6 ms: 1.07x slower                                      |
| pickle                   | 6.80 us                                                     | 7.33 us: 1.08x slower                                      |
| pathlib                  | 77.4 ms                                                     | 84.0 ms: 1.09x slower                                      |
| async_generators         | 224 ms                                                      | 246 ms: 1.10x slower                                       |
| nbody                    | 69.3 ms                                                     | 76.7 ms: 1.11x slower                                      |
| pickle_list              | 2.59 us                                                     | 2.87 us: 1.11x slower                                      |
| pickle_dict              | 16.9 us                                                     | 18.9 us: 1.12x slower                                      |
| bench_mp_pool            | 60.7 ms                                                     | 67.9 ms: 1.12x slower                                      |
| logging_format           | 6.66 us                                                     | 7.52 us: 1.13x slower                                      |
| gc_traversal             | 1.34 ms                                                     | 1.53 ms: 1.14x slower                                      |
| logging_simple           | 6.20 us                                                     | 7.05 us: 1.14x slower                                      |
| dask                     | 305 ms                                                      | 389 ms: 1.28x slower                                       |
| coverage                 | 40.0 ms                                                     | 52.0 ms: 1.30x slower                                      |
| telco                    | 3.78 ms                                                     | 5.02 ms: 1.33x slower                                      |
| Geometric mean           | (ref)                                                       | 1.12x faster                                               |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, scimark_fft, tomli_loads
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
