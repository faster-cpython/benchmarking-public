
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: a4921c7
- commit date: 2023-07-16
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 2.74 sec                                                              | 2.71 sec: 1.01x faster                                        |
| tornado_http   | 102 ms                                                                | 98.7 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 197 ms                                                                | 192 ms: 1.02x faster                                          |
| nbody          | 89.3 ms                                                               | 96.3 ms: 1.08x slower                                         |
| float          | 80.6 ms                                                               | 91.2 ms: 1.13x slower                                         |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.72 ms                                                               | 3.41 ms: 1.09x faster                                         |
| regex_dna      | 216 ms                                                                | 201 ms: 1.08x faster                                          |
| regex_v8       | 22.9 ms                                                               | 22.3 ms: 1.03x faster                                         |
| regex_compile  | 145 ms                                                                | 142 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle               | 10.9 us                                                               | 10.6 us: 1.03x faster                                         |
| unpickle_list        | 4.98 us                                                               | 4.86 us: 1.02x faster                                         |
| json_loads           | 25.2 us                                                               | 24.9 us: 1.01x faster                                         |
| xml_etree_process    | 59.4 ms                                                               | 58.8 ms: 1.01x faster                                         |
| json_dumps           | 9.86 ms                                                               | 9.76 ms: 1.01x faster                                         |
| xml_etree_iterparse  | 104 ms                                                                | 103 ms: 1.01x faster                                          |
| pickle_dict          | 31.2 us                                                               | 31.1 us: 1.00x faster                                         |
| unpickle_pure_python | 220 us                                                                | 221 us: 1.01x slower                                          |
| pickle_list          | 4.55 us                                                               | 4.62 us: 1.02x slower                                         |
| xml_etree_generate   | 85.0 ms                                                               | 86.8 ms: 1.02x slower                                         |
| tomli_loads          | 2.23 sec                                                              | 2.47 sec: 1.11x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 9.30 ms                                                               | 9.48 ms: 1.02x slower                                         |
| python_startup_no_site | 6.76 ms                                                               | 6.90 ms: 1.02x slower                                         |
| Geometric mean         | (ref)                                                                 | 1.02x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 10.6 ms                                                               | 13.4 ms: 1.27x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| unpack_sequence          | 53.5 ns                                                               | 43.2 ns: 1.24x faster                                         |
| logging_format           | 7.24 us                                                               | 6.55 us: 1.10x faster                                         |
| regex_effbot             | 3.72 ms                                                               | 3.41 ms: 1.09x faster                                         |
| logging_simple           | 6.45 us                                                               | 5.99 us: 1.08x faster                                         |
| regex_dna                | 216 ms                                                                | 201 ms: 1.08x faster                                          |
| generators               | 31.4 ms                                                               | 29.4 ms: 1.07x faster                                         |
| tornado_http             | 102 ms                                                                | 98.7 ms: 1.04x faster                                         |
| dulwich_log              | 67.9 ms                                                               | 65.5 ms: 1.04x faster                                         |
| deepcopy_reduce          | 3.29 us                                                               | 3.19 us: 1.03x faster                                         |
| pickle                   | 10.9 us                                                               | 10.6 us: 1.03x faster                                         |
| regex_v8                 | 22.9 ms                                                               | 22.3 ms: 1.03x faster                                         |
| coverage                 | 96.0 ms                                                               | 93.8 ms: 1.02x faster                                         |
| pidigits                 | 197 ms                                                                | 192 ms: 1.02x faster                                          |
| unpickle_list            | 4.98 us                                                               | 4.86 us: 1.02x faster                                         |
| dask                     | 540 ms                                                                | 529 ms: 1.02x faster                                          |
| regex_compile            | 145 ms                                                                | 142 ms: 1.02x faster                                          |
| sqlglot_normalize        | 110 ms                                                                | 108 ms: 1.02x faster                                          |
| pprint_safe_repr         | 754 ms                                                                | 742 ms: 1.02x faster                                          |
| create_gc_cycles         | 1.51 ms                                                               | 1.49 ms: 1.01x faster                                         |
| docutils                 | 2.74 sec                                                              | 2.71 sec: 1.01x faster                                        |
| json_loads               | 25.2 us                                                               | 24.9 us: 1.01x faster                                         |
| pprint_pformat           | 1.54 sec                                                              | 1.52 sec: 1.01x faster                                        |
| xml_etree_process        | 59.4 ms                                                               | 58.8 ms: 1.01x faster                                         |
| asyncio_tcp              | 514 ms                                                                | 509 ms: 1.01x faster                                          |
| json_dumps               | 9.86 ms                                                               | 9.76 ms: 1.01x faster                                         |
| deepcopy                 | 364 us                                                                | 362 us: 1.01x faster                                          |
| xml_etree_iterparse      | 104 ms                                                                | 103 ms: 1.01x faster                                          |
| pickle_dict              | 31.2 us                                                               | 31.1 us: 1.00x faster                                         |
| mypy2                    | 345 ms                                                                | 343 ms: 1.00x faster                                          |
| sqlglot_optimize         | 54.3 ms                                                               | 54.1 ms: 1.00x faster                                         |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                        |
| mdp                      | 2.56 sec                                                              | 2.57 sec: 1.00x slower                                        |
| bench_thread_pool        | 835 us                                                                | 839 us: 1.00x slower                                          |
| unpickle_pure_python     | 220 us                                                                | 221 us: 1.01x slower                                          |
| async_tree_io            | 1.23 sec                                                              | 1.24 sec: 1.01x slower                                        |
| async_tree_none          | 495 ms                                                                | 499 ms: 1.01x slower                                          |
| chaos                    | 64.0 ms                                                               | 64.6 ms: 1.01x slower                                         |
| raytrace                 | 297 ms                                                                | 299 ms: 1.01x slower                                          |
| typing_runtime_protocols | 145 us                                                                | 146 us: 1.01x slower                                          |
| pathlib                  | 18.7 ms                                                               | 18.9 ms: 1.01x slower                                         |
| async_tree_memoization   | 599 ms                                                                | 606 ms: 1.01x slower                                          |
| meteor_contest           | 104 ms                                                                | 106 ms: 1.01x slower                                          |
| telco                    | 6.88 ms                                                               | 6.98 ms: 1.02x slower                                         |
| pickle_list              | 4.55 us                                                               | 4.62 us: 1.02x slower                                         |
| sqlglot_transpile        | 1.67 ms                                                               | 1.71 ms: 1.02x slower                                         |
| python_startup           | 9.30 ms                                                               | 9.48 ms: 1.02x slower                                         |
| xml_etree_generate       | 85.0 ms                                                               | 86.8 ms: 1.02x slower                                         |
| scimark_sparse_mat_mult  | 4.99 ms                                                               | 5.10 ms: 1.02x slower                                         |
| python_startup_no_site   | 6.76 ms                                                               | 6.90 ms: 1.02x slower                                         |
| richards_super           | 50.1 ms                                                               | 51.2 ms: 1.02x slower                                         |
| sqlglot_parse            | 1.35 ms                                                               | 1.38 ms: 1.02x slower                                         |
| coroutines               | 22.1 ms                                                               | 22.7 ms: 1.03x slower                                         |
| scimark_fft              | 361 ms                                                                | 371 ms: 1.03x slower                                          |
| richards                 | 43.7 ms                                                               | 45.0 ms: 1.03x slower                                         |
| scimark_sor              | 124 ms                                                                | 128 ms: 1.03x slower                                          |
| spectral_norm            | 106 ms                                                                | 111 ms: 1.04x slower                                          |
| go                       | 137 ms                                                                | 144 ms: 1.05x slower                                          |
| nqueens                  | 82.4 ms                                                               | 86.7 ms: 1.05x slower                                         |
| nbody                    | 89.3 ms                                                               | 96.3 ms: 1.08x slower                                         |
| deltablue                | 3.51 ms                                                               | 3.79 ms: 1.08x slower                                         |
| pyflate                  | 444 ms                                                                | 480 ms: 1.08x slower                                          |
| hexiom                   | 6.21 ms                                                               | 6.82 ms: 1.10x slower                                         |
| gc_traversal             | 3.91 ms                                                               | 4.32 ms: 1.11x slower                                         |
| tomli_loads              | 2.23 sec                                                              | 2.47 sec: 1.11x slower                                        |
| crypto_pyaes             | 79.6 ms                                                               | 88.5 ms: 1.11x slower                                         |
| logging_silent           | 98.6 ns                                                               | 110 ns: 1.11x slower                                          |
| fannkuch                 | 398 ms                                                                | 448 ms: 1.13x slower                                          |
| float                    | 80.6 ms                                                               | 91.2 ms: 1.13x slower                                         |
| comprehensions           | 20.7 us                                                               | 24.7 us: 1.19x slower                                         |
| scimark_lu               | 114 ms                                                                | 142 ms: 1.25x slower                                          |
| mako                     | 10.6 ms                                                               | 13.4 ms: 1.27x slower                                         |
| deepcopy_memo            | 38.3 us                                                               | 53.6 us: 1.40x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                  |

Benchmark hidden because not significant (10): json, pickle_pure_python, scimark_monte_carlo, bench_mp_pool, async_generators, xml_etree_parse, pycparser, unpickle, async_tree_cpu_io_mixed, sqlite_synth
