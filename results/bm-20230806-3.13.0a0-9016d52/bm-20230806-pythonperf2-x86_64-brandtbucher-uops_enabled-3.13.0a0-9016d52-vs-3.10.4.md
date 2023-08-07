
# Results vs. 3.10.4

- fork: brandtbucher
- ref: uops_enabled
- machine: linux-x86_64
- commit hash: 9016d52
- commit date: 2023-08-06
- overall geometric mean: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 3.05 sec: 1.12x faster                                                    |
| tornado_http   | 152 ms                                                       | 125 ms: 1.22x faster                                                      |
| Geometric mean | (ref)                                                        | 1.17x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 98.3 ms: 1.40x faster                                                     |
| float          | 110 ms                                                       | 86.9 ms: 1.27x faster                                                     |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                        | 1.23x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 171 ms: 1.13x faster                                                      |
| regex_v8       | 26.6 ms                                                      | 24.9 ms: 1.07x faster                                                     |
| regex_dna      | 259 ms                                                       | 249 ms: 1.04x faster                                                      |
| regex_effbot   | 2.99 ms                                                      | 3.69 ms: 1.23x slower                                                     |
| Geometric mean | (ref)                                                        | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 329 us: 1.39x faster                                                      |
| json_dumps           | 14.2 ms                                                      | 10.4 ms: 1.36x faster                                                     |
| unpickle_pure_python | 321 us                                                       | 237 us: 1.36x faster                                                      |
| xml_etree_process    | 76.0 ms                                                      | 60.8 ms: 1.25x faster                                                     |
| json_loads           | 30.0 us                                                      | 25.9 us: 1.16x faster                                                     |
| xml_etree_generate   | 94.6 ms                                                      | 90.0 ms: 1.05x faster                                                     |
| tomli_loads          | 2.97 sec                                                     | 2.84 sec: 1.05x faster                                                    |
| xml_etree_parse      | 162 ms                                                       | 155 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                       | 112 ms: 1.02x slower                                                      |
| pickle               | 9.94 us                                                      | 10.2 us: 1.03x slower                                                     |
| unpickle_list        | 4.49 us                                                      | 4.68 us: 1.04x slower                                                     |
| unpickle             | 14.2 us                                                      | 14.8 us: 1.05x slower                                                     |
| pickle_list          | 4.11 us                                                      | 4.54 us: 1.11x slower                                                     |
| pickle_dict          | 30.0 us                                                      | 33.8 us: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.08x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.7 ms: 1.02x slower                                                     |
| python_startup_no_site | 7.32 ms                                                      | 8.70 ms: 1.19x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 12.3 ms: 1.20x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 159 us: 3.28x faster                                                      |
| asyncio_tcp              | 782 ms                                                       | 374 ms: 2.09x faster                                                      |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.95x faster                                                    |
| deltablue                | 7.47 ms                                                      | 3.96 ms: 1.89x faster                                                     |
| raytrace                 | 488 ms                                                       | 295 ms: 1.66x faster                                                      |
| logging_silent           | 166 ns                                                       | 101 ns: 1.65x faster                                                      |
| bench_mp_pool            | 7.18 ms                                                      | 4.55 ms: 1.58x faster                                                     |
| chaos                    | 107 ms                                                       | 68.0 ms: 1.57x faster                                                     |
| scimark_monte_carlo      | 109 ms                                                       | 71.0 ms: 1.54x faster                                                     |
| generators               | 58.0 ms                                                      | 38.0 ms: 1.53x faster                                                     |
| crypto_pyaes             | 118 ms                                                       | 77.6 ms: 1.52x faster                                                     |
| scimark_lu               | 164 ms                                                       | 107 ms: 1.52x faster                                                      |
| sqlglot_parse            | 2.26 ms                                                      | 1.49 ms: 1.52x faster                                                     |
| async_tree_none          | 700 ms                                                       | 478 ms: 1.46x faster                                                      |
| richards_super           | 90.8 ms                                                      | 62.1 ms: 1.46x faster                                                     |
| async_tree_io            | 1.61 sec                                                     | 1.10 sec: 1.46x faster                                                    |
| async_tree_memoization   | 824 ms                                                       | 578 ms: 1.43x faster                                                      |
| sqlglot_transpile        | 2.71 ms                                                      | 1.91 ms: 1.42x faster                                                     |
| nbody                    | 137 ms                                                       | 98.3 ms: 1.40x faster                                                     |
| pickle_pure_python       | 457 us                                                       | 329 us: 1.39x faster                                                      |
| go                       | 259 ms                                                       | 188 ms: 1.38x faster                                                      |
| json_dumps               | 14.2 ms                                                      | 10.4 ms: 1.36x faster                                                     |
| unpickle_pure_python     | 321 us                                                       | 237 us: 1.36x faster                                                      |
| spectral_norm            | 136 ms                                                       | 101 ms: 1.35x faster                                                      |
| richards                 | 74.1 ms                                                      | 55.7 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 727 ms: 1.31x faster                                                      |
| logging_simple           | 8.90 us                                                      | 6.91 us: 1.29x faster                                                     |
| coroutines               | 30.4 ms                                                      | 23.9 ms: 1.27x faster                                                     |
| logging_format           | 9.57 us                                                      | 7.53 us: 1.27x faster                                                     |
| float                    | 110 ms                                                       | 86.9 ms: 1.27x faster                                                     |
| pprint_pformat           | 2.15 sec                                                     | 1.71 sec: 1.26x faster                                                    |
| pprint_safe_repr         | 1.05 sec                                                     | 839 ms: 1.25x faster                                                      |
| xml_etree_process        | 76.0 ms                                                      | 60.8 ms: 1.25x faster                                                     |
| pyflate                  | 697 ms                                                       | 559 ms: 1.25x faster                                                      |
| tornado_http             | 152 ms                                                       | 125 ms: 1.22x faster                                                      |
| mypy2                    | 466 ms                                                       | 386 ms: 1.21x faster                                                      |
| pycparser                | 1.66 sec                                                     | 1.38 sec: 1.21x faster                                                    |
| mako                     | 14.7 ms                                                      | 12.3 ms: 1.20x faster                                                     |
| sqlglot_normalize        | 144 ms                                                       | 122 ms: 1.18x faster                                                      |
| scimark_sor              | 177 ms                                                       | 151 ms: 1.17x faster                                                      |
| json_loads               | 30.0 us                                                      | 25.9 us: 1.16x faster                                                     |
| deepcopy                 | 454 us                                                       | 395 us: 1.15x faster                                                      |
| deepcopy_reduce          | 4.03 us                                                      | 3.51 us: 1.15x faster                                                     |
| bench_thread_pool        | 1.14 ms                                                      | 998 us: 1.14x faster                                                      |
| dulwich_log              | 80.1 ms                                                      | 70.5 ms: 1.13x faster                                                     |
| regex_compile            | 194 ms                                                       | 171 ms: 1.13x faster                                                      |
| json                     | 5.96 ms                                                      | 5.29 ms: 1.13x faster                                                     |
| sqlglot_optimize         | 70.3 ms                                                      | 62.5 ms: 1.12x faster                                                     |
| hexiom                   | 9.52 ms                                                      | 8.48 ms: 1.12x faster                                                     |
| mdp                      | 3.03 sec                                                     | 2.71 sec: 1.12x faster                                                    |
| docutils                 | 3.40 sec                                                     | 3.05 sec: 1.12x faster                                                    |
| pathlib                  | 21.7 ms                                                      | 19.6 ms: 1.10x faster                                                     |
| deepcopy_memo            | 48.9 us                                                      | 44.3 us: 1.10x faster                                                     |
| create_gc_cycles         | 1.82 ms                                                      | 1.67 ms: 1.09x faster                                                     |
| regex_v8                 | 26.6 ms                                                      | 24.9 ms: 1.07x faster                                                     |
| unpack_sequence          | 59.5 ns                                                      | 55.7 ns: 1.07x faster                                                     |
| sqlite_synth             | 2.97 us                                                      | 2.78 us: 1.07x faster                                                     |
| xml_etree_generate       | 94.6 ms                                                      | 90.0 ms: 1.05x faster                                                     |
| tomli_loads              | 2.97 sec                                                     | 2.84 sec: 1.05x faster                                                    |
| regex_dna                | 259 ms                                                       | 249 ms: 1.04x faster                                                      |
| xml_etree_parse          | 162 ms                                                       | 155 ms: 1.04x faster                                                      |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                                      |
| scimark_fft              | 359 ms                                                       | 349 ms: 1.03x faster                                                      |
| fannkuch                 | 496 ms                                                       | 482 ms: 1.03x faster                                                      |
| async_generators         | 422 ms                                                       | 410 ms: 1.03x faster                                                      |
| nqueens                  | 112 ms                                                       | 114 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 110 ms                                                       | 112 ms: 1.02x slower                                                      |
| python_startup           | 11.5 ms                                                      | 11.7 ms: 1.02x slower                                                     |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.03x slower                                                     |
| comprehensions           | 26.9 us                                                      | 27.9 us: 1.03x slower                                                     |
| unpickle_list            | 4.49 us                                                      | 4.68 us: 1.04x slower                                                     |
| unpickle                 | 14.2 us                                                      | 14.8 us: 1.05x slower                                                     |
| meteor_contest           | 137 ms                                                       | 144 ms: 1.06x slower                                                      |
| pickle_list              | 4.11 us                                                      | 4.54 us: 1.11x slower                                                     |
| pickle_dict              | 30.0 us                                                      | 33.8 us: 1.13x slower                                                     |
| gc_traversal             | 3.45 ms                                                      | 3.92 ms: 1.14x slower                                                     |
| telco                    | 7.14 ms                                                      | 8.30 ms: 1.16x slower                                                     |
| python_startup_no_site   | 7.32 ms                                                      | 8.70 ms: 1.19x slower                                                     |
| regex_effbot             | 2.99 ms                                                      | 3.69 ms: 1.23x slower                                                     |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 6.61 ms: 1.27x slower                                                     |
| dask                     | 463 ms                                                       | 603 ms: 1.30x slower                                                      |
| coverage                 | 64.0 ms                                                      | 90.8 ms: 1.42x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.20x faster                                                              |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
