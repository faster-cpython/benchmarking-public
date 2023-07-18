
# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin
- machine: windows-amd64
- commit hash: ba47232
- commit date: 2023-07-17
- overall geometric mean: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.62 sec: 1.17x faster                                             |
| tornado_http   | 109 ms                                                      | 88.6 ms: 1.23x faster                                              |
| Geometric mean | (ref)                                                       | 1.20x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 50.5 ms: 1.19x faster                                              |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                               |
| nbody          | 69.3 ms                                                     | 72.3 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                       | 1.03x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 88.6 ms: 1.17x faster                                              |
| regex_dna      | 132 ms                                                      | 126 ms: 1.05x faster                                               |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                              |
| regex_v8       | 15.0 ms                                                     | 26.0 ms: 1.73x slower                                              |
| Geometric mean | (ref)                                                       | 1.08x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.67 ms: 1.50x faster                                              |
| pickle_pure_python   | 257 us                                                      | 197 us: 1.30x faster                                               |
| unpickle_pure_python | 171 us                                                      | 137 us: 1.25x faster                                               |
| tomli_loads          | 1.62 sec                                                    | 1.36 sec: 1.19x faster                                             |
| xml_etree_process    | 43.4 ms                                                     | 38.4 ms: 1.13x faster                                              |
| unpickle             | 9.17 us                                                     | 8.30 us: 1.11x faster                                              |
| xml_etree_parse      | 102 ms                                                      | 92.5 ms: 1.10x faster                                              |
| json_loads           | 14.2 us                                                     | 13.7 us: 1.04x faster                                              |
| xml_etree_generate   | 54.5 ms                                                     | 55.4 ms: 1.02x slower                                              |
| xml_etree_iterparse  | 63.5 ms                                                     | 64.6 ms: 1.02x slower                                              |
| unpickle_list        | 2.81 us                                                     | 2.89 us: 1.03x slower                                              |
| pickle               | 6.80 us                                                     | 7.20 us: 1.06x slower                                              |
| pickle_dict          | 16.9 us                                                     | 18.5 us: 1.09x slower                                              |
| pickle_list          | 2.59 us                                                     | 2.87 us: 1.11x slower                                              |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 21.1 ms: 1.06x slower                                              |
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                              |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|-----------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.42 ms: 1.37x faster                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 97.8 us: 3.32x faster                                              |
| deltablue                | 4.17 ms                                                     | 2.12 ms: 1.97x faster                                              |
| richards_super           | 51.7 ms                                                     | 29.6 ms: 1.75x faster                                              |
| mypy2                    | 352 ms                                                      | 215 ms: 1.64x faster                                               |
| richards                 | 41.2 ms                                                     | 26.1 ms: 1.58x faster                                              |
| logging_silent           | 96.4 ns                                                     | 61.8 ns: 1.56x faster                                              |
| go                       | 136 ms                                                      | 88.5 ms: 1.54x faster                                              |
| scimark_lu               | 85.4 ms                                                     | 56.8 ms: 1.50x faster                                              |
| json_dumps               | 8.50 ms                                                     | 5.67 ms: 1.50x faster                                              |
| asyncio_tcp              | 712 ms                                                      | 476 ms: 1.50x faster                                               |
| sqlglot_parse            | 1.22 ms                                                     | 821 us: 1.48x faster                                               |
| async_tree_io            | 1.07 sec                                                    | 733 ms: 1.45x faster                                               |
| async_tree_memoization   | 497 ms                                                      | 344 ms: 1.44x faster                                               |
| async_tree_none          | 420 ms                                                      | 293 ms: 1.43x faster                                               |
| sqlglot_transpile        | 1.46 ms                                                     | 1.04 ms: 1.41x faster                                              |
| raytrace                 | 271 ms                                                      | 195 ms: 1.39x faster                                               |
| generators               | 31.6 ms                                                     | 23.0 ms: 1.37x faster                                              |
| mako                     | 8.80 ms                                                     | 6.42 ms: 1.37x faster                                              |
| pyflate                  | 387 ms                                                      | 286 ms: 1.35x faster                                               |
| chaos                    | 58.9 ms                                                     | 44.1 ms: 1.34x faster                                              |
| pickle_pure_python       | 257 us                                                      | 197 us: 1.30x faster                                               |
| scimark_monte_carlo      | 55.9 ms                                                     | 43.4 ms: 1.29x faster                                              |
| scimark_sor              | 105 ms                                                      | 82.3 ms: 1.27x faster                                              |
| pycparser                | 868 ms                                                      | 683 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 481 ms: 1.27x faster                                               |
| hexiom                   | 5.52 ms                                                     | 4.41 ms: 1.25x faster                                              |
| unpickle_pure_python     | 171 us                                                      | 137 us: 1.25x faster                                               |
| crypto_pyaes             | 62.3 ms                                                     | 50.5 ms: 1.23x faster                                              |
| tornado_http             | 109 ms                                                      | 88.6 ms: 1.23x faster                                              |
| deepcopy_memo            | 28.5 us                                                     | 23.5 us: 1.22x faster                                              |
| tomli_loads              | 1.62 sec                                                    | 1.36 sec: 1.19x faster                                             |
| float                    | 60.2 ms                                                     | 50.5 ms: 1.19x faster                                              |
| spectral_norm            | 78.0 ms                                                     | 65.5 ms: 1.19x faster                                              |
| regex_compile            | 103 ms                                                      | 88.6 ms: 1.17x faster                                              |
| docutils                 | 1.89 sec                                                    | 1.62 sec: 1.17x faster                                             |
| pprint_pformat           | 1.21 sec                                                    | 1.04 sec: 1.16x faster                                             |
| pprint_safe_repr         | 589 ms                                                      | 509 ms: 1.16x faster                                               |
| bench_thread_pool        | 946 us                                                      | 829 us: 1.14x faster                                               |
| mdp                      | 1.71 sec                                                    | 1.51 sec: 1.14x faster                                             |
| xml_etree_process        | 43.4 ms                                                     | 38.4 ms: 1.13x faster                                              |
| sqlglot_optimize         | 39.0 ms                                                     | 34.5 ms: 1.13x faster                                              |
| comprehensions           | 16.0 us                                                     | 14.3 us: 1.11x faster                                              |
| unpickle                 | 9.17 us                                                     | 8.30 us: 1.11x faster                                              |
| xml_etree_parse          | 102 ms                                                      | 92.5 ms: 1.10x faster                                              |
| create_gc_cycles         | 782 us                                                      | 714 us: 1.09x faster                                               |
| dulwich_log              | 47.6 ms                                                     | 43.6 ms: 1.09x faster                                              |
| coroutines               | 15.9 ms                                                     | 14.7 ms: 1.09x faster                                              |
| sqlglot_normalize        | 202 ms                                                      | 187 ms: 1.08x faster                                               |
| nqueens                  | 67.0 ms                                                     | 62.7 ms: 1.07x faster                                              |
| scimark_fft              | 193 ms                                                      | 181 ms: 1.07x faster                                               |
| sqlite_synth             | 1.84 us                                                     | 1.72 us: 1.07x faster                                              |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.51 ms: 1.06x faster                                              |
| deepcopy                 | 255 us                                                      | 241 us: 1.06x faster                                               |
| json                     | 3.05 ms                                                     | 2.88 ms: 1.06x faster                                              |
| fannkuch                 | 258 ms                                                      | 245 ms: 1.05x faster                                               |
| regex_dna                | 132 ms                                                      | 126 ms: 1.05x faster                                               |
| json_loads               | 14.2 us                                                     | 13.7 us: 1.04x faster                                              |
| deepcopy_reduce          | 2.16 us                                                     | 2.08 us: 1.03x faster                                              |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 1.97 sec: 1.03x faster                                             |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                              |
| unpack_sequence          | 37.8 ns                                                     | 37.4 ns: 1.01x faster                                              |
| xml_etree_generate       | 54.5 ms                                                     | 55.4 ms: 1.02x slower                                              |
| xml_etree_iterparse      | 63.5 ms                                                     | 64.6 ms: 1.02x slower                                              |
| pathlib                  | 77.4 ms                                                     | 79.4 ms: 1.03x slower                                              |
| unpickle_list            | 2.81 us                                                     | 2.89 us: 1.03x slower                                              |
| pidigits                 | 145 ms                                                      | 150 ms: 1.03x slower                                               |
| meteor_contest           | 72.5 ms                                                     | 75.1 ms: 1.04x slower                                              |
| logging_format           | 6.66 us                                                     | 6.90 us: 1.04x slower                                              |
| logging_simple           | 6.20 us                                                     | 6.46 us: 1.04x slower                                              |
| nbody                    | 69.3 ms                                                     | 72.3 ms: 1.04x slower                                              |
| python_startup           | 20.0 ms                                                     | 21.1 ms: 1.06x slower                                              |
| pickle                   | 6.80 us                                                     | 7.20 us: 1.06x slower                                              |
| telco                    | 3.78 ms                                                     | 4.02 ms: 1.06x slower                                              |
| async_generators         | 224 ms                                                      | 244 ms: 1.09x slower                                               |
| pickle_dict              | 16.9 us                                                     | 18.5 us: 1.09x slower                                              |
| gc_traversal             | 1.34 ms                                                     | 1.47 ms: 1.09x slower                                              |
| pickle_list              | 2.59 us                                                     | 2.87 us: 1.11x slower                                              |
| bench_mp_pool            | 60.7 ms                                                     | 69.6 ms: 1.15x slower                                              |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                              |
| dask                     | 305 ms                                                      | 364 ms: 1.19x slower                                               |
| coverage                 | 40.0 ms                                                     | 50.8 ms: 1.27x slower                                              |
| regex_v8                 | 15.0 ms                                                     | 26.0 ms: 1.73x slower                                              |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                       |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
