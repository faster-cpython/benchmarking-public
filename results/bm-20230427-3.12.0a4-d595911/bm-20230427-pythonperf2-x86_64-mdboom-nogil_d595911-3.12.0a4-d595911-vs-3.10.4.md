
# Results vs. 3.10.4

- fork: mdboom
- ref: nogil_d595911
- machine: linux-x86_64
- commit hash: d595911
- commit date: 2023-04-27
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 303 ms: 1.15x faster                                                 |
| chameleon      | 9.72 ms                                                      | 8.37 ms: 1.16x faster                                                |
| docutils       | 3.40 sec                                                     | 2.99 sec: 1.14x faster                                               |
| html5lib       | 94.6 ms                                                      | 73.1 ms: 1.29x faster                                                |
| Geometric mean | (ref)                                                        | 1.19x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 110 ms                                                       | 65.5 ms: 1.68x faster                                                |
| nbody          | 137 ms                                                       | 102 ms: 1.35x faster                                                 |
| pidigits       | 271 ms                                                       | 246 ms: 1.10x faster                                                 |
| Geometric mean | (ref)                                                        | 1.36x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 157 ms: 1.24x faster                                                 |
| regex_v8       | 26.6 ms                                                      | 23.1 ms: 1.15x faster                                                |
| regex_dna      | 259 ms                                                       | 233 ms: 1.11x faster                                                 |
| regex_effbot   | 2.99 ms                                                      | 3.30 ms: 1.10x slower                                                |
| Geometric mean | (ref)                                                        | 1.10x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 329 us: 1.39x faster                                                 |
| unpickle_pure_python | 321 us                                                       | 233 us: 1.38x faster                                                 |
| json_dumps           | 14.2 ms                                                      | 11.4 ms: 1.24x faster                                                |
| xml_etree_process    | 76.0 ms                                                      | 62.8 ms: 1.21x faster                                                |
| tomli_loads          | 2.97 sec                                                     | 2.49 sec: 1.19x faster                                               |
| xml_etree_parse      | 162 ms                                                       | 137 ms: 1.18x faster                                                 |
| xml_etree_generate   | 94.6 ms                                                      | 85.4 ms: 1.11x faster                                                |
| pickle               | 9.94 us                                                      | 9.64 us: 1.03x faster                                                |
| json_loads           | 30.0 us                                                      | 32.3 us: 1.08x slower                                                |
| pickle_list          | 4.11 us                                                      | 4.46 us: 1.08x slower                                                |
| pickle_dict          | 30.0 us                                                      | 32.7 us: 1.09x slower                                                |
| unpickle             | 14.2 us                                                      | 15.8 us: 1.11x slower                                                |
| unpickle_list        | 4.49 us                                                      | 5.01 us: 1.11x slower                                                |
| xml_etree_iterparse  | 110 ms                                                       | 126 ms: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.5 ms: 1.00x slower                                                |
| python_startup_no_site | 7.32 ms                                                      | 8.45 ms: 1.15x slower                                                |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 51.5 ms                                                      | 40.6 ms: 1.27x faster                                                |
| genshi_xml      | 64.7 ms                                                      | 54.6 ms: 1.19x faster                                                |
| genshi_text     | 31.5 ms                                                      | 27.0 ms: 1.17x faster                                                |
| mako            | 14.7 ms                                                      | 14.9 ms: 1.02x slower                                                |
| Geometric mean  | (ref)                                                        | 1.15x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-pythonperf2-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io            | 1.61 sec                                                     | 595 ms: 2.70x faster                                                 |
| async_tree_none          | 700 ms                                                       | 304 ms: 2.30x faster                                                 |
| async_tree_memoization   | 824 ms                                                       | 361 ms: 2.28x faster                                                 |
| asyncio_tcp              | 782 ms                                                       | 399 ms: 1.96x faster                                                 |
| deltablue                | 7.47 ms                                                      | 4.00 ms: 1.87x faster                                                |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.70 sec: 1.82x faster                                               |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 529 ms: 1.80x faster                                                 |
| float                    | 110 ms                                                       | 65.5 ms: 1.68x faster                                                |
| logging_silent           | 166 ns                                                       | 99.0 ns: 1.67x faster                                                |
| go                       | 259 ms                                                       | 169 ms: 1.53x faster                                                 |
| scimark_lu               | 164 ms                                                       | 108 ms: 1.51x faster                                                 |
| scimark_sor              | 177 ms                                                       | 117 ms: 1.51x faster                                                 |
| pyflate                  | 697 ms                                                       | 482 ms: 1.45x faster                                                 |
| pickle_pure_python       | 457 us                                                       | 329 us: 1.39x faster                                                 |
| richards                 | 74.1 ms                                                      | 53.5 ms: 1.38x faster                                                |
| chaos                    | 107 ms                                                       | 77.8 ms: 1.38x faster                                                |
| unpickle_pure_python     | 321 us                                                       | 233 us: 1.38x faster                                                 |
| richards_super           | 90.8 ms                                                      | 66.5 ms: 1.37x faster                                                |
| pycparser                | 1.66 sec                                                     | 1.22 sec: 1.36x faster                                               |
| hexiom                   | 9.52 ms                                                      | 7.01 ms: 1.36x faster                                                |
| nbody                    | 137 ms                                                       | 102 ms: 1.35x faster                                                 |
| crypto_pyaes             | 118 ms                                                       | 88.9 ms: 1.33x faster                                                |
| scimark_monte_carlo      | 109 ms                                                       | 82.9 ms: 1.32x faster                                                |
| sqlglot_parse            | 2.26 ms                                                      | 1.73 ms: 1.31x faster                                                |
| sqlglot_transpile        | 2.71 ms                                                      | 2.08 ms: 1.30x faster                                                |
| raytrace                 | 488 ms                                                       | 376 ms: 1.30x faster                                                 |
| spectral_norm            | 136 ms                                                       | 105 ms: 1.30x faster                                                 |
| html5lib                 | 94.6 ms                                                      | 73.1 ms: 1.29x faster                                                |
| django_template          | 51.5 ms                                                      | 40.6 ms: 1.27x faster                                                |
| async_generators         | 422 ms                                                       | 335 ms: 1.26x faster                                                 |
| json_dumps               | 14.2 ms                                                      | 11.4 ms: 1.24x faster                                                |
| regex_compile            | 194 ms                                                       | 157 ms: 1.24x faster                                                 |
| thrift                   | 1.16 ms                                                      | 957 us: 1.22x faster                                                 |
| logging_simple           | 8.90 us                                                      | 7.32 us: 1.22x faster                                                |
| xml_etree_process        | 76.0 ms                                                      | 62.8 ms: 1.21x faster                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 871 ms: 1.20x faster                                                 |
| deepcopy_memo            | 48.9 us                                                      | 41.0 us: 1.19x faster                                                |
| pprint_pformat           | 2.15 sec                                                     | 1.81 sec: 1.19x faster                                               |
| tomli_loads              | 2.97 sec                                                     | 2.49 sec: 1.19x faster                                               |
| dulwich_log              | 80.1 ms                                                      | 67.2 ms: 1.19x faster                                                |
| genshi_xml               | 64.7 ms                                                      | 54.6 ms: 1.19x faster                                                |
| xml_etree_parse          | 162 ms                                                       | 137 ms: 1.18x faster                                                 |
| logging_format           | 9.57 us                                                      | 8.16 us: 1.17x faster                                                |
| sqlglot_normalize        | 144 ms                                                       | 123 ms: 1.17x faster                                                 |
| sqlglot_optimize         | 70.3 ms                                                      | 59.9 ms: 1.17x faster                                                |
| genshi_text              | 31.5 ms                                                      | 27.0 ms: 1.17x faster                                                |
| chameleon                | 9.72 ms                                                      | 8.37 ms: 1.16x faster                                                |
| regex_v8                 | 26.6 ms                                                      | 23.1 ms: 1.15x faster                                                |
| 2to3                     | 350 ms                                                       | 303 ms: 1.15x faster                                                 |
| docutils                 | 3.40 sec                                                     | 2.99 sec: 1.14x faster                                               |
| unpack_sequence          | 59.5 ns                                                      | 52.4 ns: 1.14x faster                                                |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.58 ms: 1.14x faster                                                |
| deepcopy                 | 454 us                                                       | 403 us: 1.13x faster                                                 |
| nqueens                  | 112 ms                                                       | 99.8 ms: 1.13x faster                                                |
| gc_traversal             | 3.45 ms                                                      | 3.08 ms: 1.12x faster                                                |
| regex_dna                | 259 ms                                                       | 233 ms: 1.11x faster                                                 |
| fannkuch                 | 496 ms                                                       | 447 ms: 1.11x faster                                                 |
| xml_etree_generate       | 94.6 ms                                                      | 85.4 ms: 1.11x faster                                                |
| scimark_fft              | 359 ms                                                       | 327 ms: 1.10x faster                                                 |
| pidigits                 | 271 ms                                                       | 246 ms: 1.10x faster                                                 |
| pathlib                  | 21.7 ms                                                      | 19.8 ms: 1.09x faster                                                |
| coroutines               | 30.4 ms                                                      | 28.1 ms: 1.08x faster                                                |
| deepcopy_reduce          | 4.03 us                                                      | 3.74 us: 1.08x faster                                                |
| mdp                      | 3.03 sec                                                     | 2.82 sec: 1.08x faster                                               |
| sympy_expand             | 599 ms                                                       | 562 ms: 1.07x faster                                                 |
| sympy_integrate          | 28.1 ms                                                      | 26.4 ms: 1.06x faster                                                |
| mypy2                    | 466 ms                                                       | 449 ms: 1.04x faster                                                 |
| sympy_str                | 358 ms                                                       | 344 ms: 1.04x faster                                                 |
| pickle                   | 9.94 us                                                      | 9.64 us: 1.03x faster                                                |
| sqlite_synth             | 2.97 us                                                      | 2.88 us: 1.03x faster                                                |
| sympy_sum                | 193 ms                                                       | 191 ms: 1.01x faster                                                 |
| python_startup           | 11.5 ms                                                      | 11.5 ms: 1.00x slower                                                |
| mako                     | 14.7 ms                                                      | 14.9 ms: 1.02x slower                                                |
| telco                    | 7.14 ms                                                      | 7.29 ms: 1.02x slower                                                |
| json                     | 5.96 ms                                                      | 6.28 ms: 1.05x slower                                                |
| create_gc_cycles         | 1.82 ms                                                      | 1.93 ms: 1.06x slower                                                |
| generators               | 58.0 ms                                                      | 62.3 ms: 1.08x slower                                                |
| json_loads               | 30.0 us                                                      | 32.3 us: 1.08x slower                                                |
| bench_mp_pool            | 7.18 ms                                                      | 7.77 ms: 1.08x slower                                                |
| pickle_list              | 4.11 us                                                      | 4.46 us: 1.08x slower                                                |
| pickle_dict              | 30.0 us                                                      | 32.7 us: 1.09x slower                                                |
| comprehensions           | 26.9 us                                                      | 29.6 us: 1.10x slower                                                |
| typing_runtime_protocols | 523 us                                                       | 575 us: 1.10x slower                                                 |
| regex_effbot             | 2.99 ms                                                      | 3.30 ms: 1.10x slower                                                |
| unpickle                 | 14.2 us                                                      | 15.8 us: 1.11x slower                                                |
| unpickle_list            | 4.49 us                                                      | 5.01 us: 1.11x slower                                                |
| meteor_contest           | 137 ms                                                       | 153 ms: 1.12x slower                                                 |
| xml_etree_iterparse      | 110 ms                                                       | 126 ms: 1.14x slower                                                 |
| python_startup_no_site   | 7.32 ms                                                      | 8.45 ms: 1.15x slower                                                |
| coverage                 | 64.0 ms                                                      | 97.6 ms: 1.53x slower                                                |
| bench_thread_pool        | 1.14 ms                                                      | 2.03 ms: 1.78x slower                                                |
| Geometric mean           | (ref)                                                        | 1.18x faster                                                         |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x
