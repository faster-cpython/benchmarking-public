
# Results vs. 3.10.4

- fork: python
- ref: 22988c323ad621b9f47b
- machine: windows-amd64
- commit hash: 22988c3
- commit date: 2023-07-10
- overall geometric mean: 1.13x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                                     |
| tornado_http   | 109 ms                                                      | 98.7 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 55.7 ms: 1.08x faster                                                      |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                                       |
| nbody          | 69.3 ms                                                     | 75.9 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 93.5 ms: 1.11x faster                                                      |
| regex_dna      | 132 ms                                                      | 121 ms: 1.09x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.77 ms: 1.47x faster                                                      |
| pickle_pure_python   | 257 us                                                      | 200 us: 1.28x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 141 us: 1.21x faster                                                       |
| xml_etree_process    | 43.4 ms                                                     | 38.8 ms: 1.12x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 91.2 ms: 1.12x faster                                                      |
| unpickle             | 9.17 us                                                     | 8.45 us: 1.09x faster                                                      |
| json_loads           | 14.2 us                                                     | 13.6 us: 1.04x faster                                                      |
| tomli_loads          | 1.62 sec                                                    | 1.59 sec: 1.02x faster                                                     |
| xml_etree_iterparse  | 63.5 ms                                                     | 64.4 ms: 1.01x slower                                                      |
| xml_etree_generate   | 54.5 ms                                                     | 55.9 ms: 1.02x slower                                                      |
| unpickle_list        | 2.81 us                                                     | 2.94 us: 1.05x slower                                                      |
| pickle               | 6.80 us                                                     | 7.12 us: 1.05x slower                                                      |
| pickle_dict          | 16.9 us                                                     | 18.2 us: 1.08x slower                                                      |
| pickle_list          | 2.59 us                                                     | 2.82 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 16.9 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.47 ms: 1.18x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 96.7 us: 3.36x faster                                                      |
| deltablue                | 4.17 ms                                                     | 2.31 ms: 1.80x faster                                                      |
| mypy2                    | 352 ms                                                      | 223 ms: 1.58x faster                                                       |
| richards_super           | 51.7 ms                                                     | 34.2 ms: 1.51x faster                                                      |
| logging_silent           | 96.4 ns                                                     | 64.4 ns: 1.50x faster                                                      |
| raytrace                 | 271 ms                                                      | 182 ms: 1.49x faster                                                       |
| json_dumps               | 8.50 ms                                                     | 5.77 ms: 1.47x faster                                                      |
| async_tree_io            | 1.07 sec                                                    | 743 ms: 1.43x faster                                                       |
| async_tree_memoization   | 497 ms                                                      | 352 ms: 1.41x faster                                                       |
| async_tree_none          | 420 ms                                                      | 297 ms: 1.41x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 875 us: 1.39x faster                                                       |
| go                       | 136 ms                                                      | 98.4 ms: 1.38x faster                                                      |
| scimark_lu               | 85.4 ms                                                     | 61.8 ms: 1.38x faster                                                      |
| crypto_pyaes             | 62.3 ms                                                     | 45.4 ms: 1.37x faster                                                      |
| chaos                    | 58.9 ms                                                     | 43.1 ms: 1.37x faster                                                      |
| richards                 | 41.2 ms                                                     | 30.1 ms: 1.37x faster                                                      |
| sqlglot_transpile        | 1.46 ms                                                     | 1.10 ms: 1.33x faster                                                      |
| asyncio_tcp              | 712 ms                                                      | 545 ms: 1.31x faster                                                       |
| pickle_pure_python       | 257 us                                                      | 200 us: 1.28x faster                                                       |
| generators               | 31.6 ms                                                     | 24.6 ms: 1.28x faster                                                      |
| scimark_monte_carlo      | 55.9 ms                                                     | 43.9 ms: 1.27x faster                                                      |
| hexiom                   | 5.52 ms                                                     | 4.39 ms: 1.26x faster                                                      |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 490 ms: 1.24x faster                                                       |
| scimark_sor              | 105 ms                                                      | 84.4 ms: 1.24x faster                                                      |
| pyflate                  | 387 ms                                                      | 315 ms: 1.23x faster                                                       |
| unpickle_pure_python     | 171 us                                                      | 141 us: 1.21x faster                                                       |
| mdp                      | 1.71 sec                                                    | 1.43 sec: 1.20x faster                                                     |
| mako                     | 8.80 ms                                                     | 7.47 ms: 1.18x faster                                                      |
| spectral_norm            | 78.0 ms                                                     | 66.3 ms: 1.18x faster                                                      |
| pycparser                | 868 ms                                                      | 738 ms: 1.18x faster                                                       |
| docutils                 | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                                     |
| xml_etree_process        | 43.4 ms                                                     | 38.8 ms: 1.12x faster                                                      |
| xml_etree_parse          | 102 ms                                                      | 91.2 ms: 1.12x faster                                                      |
| bench_thread_pool        | 946 us                                                      | 851 us: 1.11x faster                                                       |
| deepcopy_memo            | 28.5 us                                                     | 25.7 us: 1.11x faster                                                      |
| pprint_safe_repr         | 589 ms                                                      | 532 ms: 1.11x faster                                                       |
| pprint_pformat           | 1.21 sec                                                    | 1.09 sec: 1.11x faster                                                     |
| regex_compile            | 103 ms                                                      | 93.5 ms: 1.11x faster                                                      |
| tornado_http             | 109 ms                                                      | 98.7 ms: 1.11x faster                                                      |
| regex_dna                | 132 ms                                                      | 121 ms: 1.09x faster                                                       |
| unpickle                 | 9.17 us                                                     | 8.45 us: 1.09x faster                                                      |
| sqlglot_optimize         | 39.0 ms                                                     | 36.0 ms: 1.08x faster                                                      |
| float                    | 60.2 ms                                                     | 55.7 ms: 1.08x faster                                                      |
| json                     | 3.05 ms                                                     | 2.83 ms: 1.08x faster                                                      |
| create_gc_cycles         | 782 us                                                      | 729 us: 1.07x faster                                                       |
| nqueens                  | 67.0 ms                                                     | 62.8 ms: 1.07x faster                                                      |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.52 ms: 1.05x faster                                                      |
| comprehensions           | 16.0 us                                                     | 15.2 us: 1.05x faster                                                      |
| sqlite_synth             | 1.84 us                                                     | 1.76 us: 1.05x faster                                                      |
| sqlglot_normalize        | 202 ms                                                      | 193 ms: 1.05x faster                                                       |
| dulwich_log              | 47.6 ms                                                     | 45.8 ms: 1.04x faster                                                      |
| json_loads               | 14.2 us                                                     | 13.6 us: 1.04x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| scimark_fft              | 193 ms                                                      | 187 ms: 1.03x faster                                                       |
| coroutines               | 15.9 ms                                                     | 15.5 ms: 1.03x faster                                                      |
| deepcopy                 | 255 us                                                      | 249 us: 1.03x faster                                                       |
| tomli_loads              | 1.62 sec                                                    | 1.59 sec: 1.02x faster                                                     |
| deepcopy_reduce          | 2.16 us                                                     | 2.18 us: 1.01x slower                                                      |
| xml_etree_iterparse      | 63.5 ms                                                     | 64.4 ms: 1.01x slower                                                      |
| xml_etree_generate       | 54.5 ms                                                     | 55.9 ms: 1.02x slower                                                      |
| meteor_contest           | 72.5 ms                                                     | 74.8 ms: 1.03x slower                                                      |
| pidigits                 | 145 ms                                                      | 150 ms: 1.03x slower                                                       |
| unpickle_list            | 2.81 us                                                     | 2.94 us: 1.05x slower                                                      |
| pickle                   | 6.80 us                                                     | 7.12 us: 1.05x slower                                                      |
| pathlib                  | 77.4 ms                                                     | 83.1 ms: 1.07x slower                                                      |
| pickle_dict              | 16.9 us                                                     | 18.2 us: 1.08x slower                                                      |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 2.20 sec: 1.08x slower                                                     |
| async_generators         | 224 ms                                                      | 243 ms: 1.09x slower                                                       |
| unpack_sequence          | 37.8 ns                                                     | 41.1 ns: 1.09x slower                                                      |
| pickle_list              | 2.59 us                                                     | 2.82 us: 1.09x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 16.9 ms: 1.09x slower                                                      |
| logging_simple           | 6.20 us                                                     | 6.78 us: 1.09x slower                                                      |
| nbody                    | 69.3 ms                                                     | 75.9 ms: 1.10x slower                                                      |
| logging_format           | 6.66 us                                                     | 7.30 us: 1.10x slower                                                      |
| bench_mp_pool            | 60.7 ms                                                     | 66.9 ms: 1.10x slower                                                      |
| gc_traversal             | 1.34 ms                                                     | 1.50 ms: 1.12x slower                                                      |
| telco                    | 3.78 ms                                                     | 4.72 ms: 1.25x slower                                                      |
| dask                     | 305 ms                                                      | 388 ms: 1.27x slower                                                       |
| coverage                 | 40.0 ms                                                     | 51.5 ms: 1.29x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                               |

Benchmark hidden because not significant (3): regex_v8, python_startup, fannkuch
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
