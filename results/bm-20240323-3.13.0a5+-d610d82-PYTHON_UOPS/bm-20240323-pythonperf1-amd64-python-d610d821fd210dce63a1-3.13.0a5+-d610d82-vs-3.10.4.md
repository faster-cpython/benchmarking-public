# Results vs. 3.10.4

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-amd64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.89 ms: 1.18x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.8 ms: 1.31x faster                                                       |
| tornado_http   | 108 ms                                                      | 87.1 ms: 1.24x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 222 ms: 1.96x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 276 ms: 1.91x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 586 ms: 1.89x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 387 ms: 1.65x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.85x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 57.1 ms: 1.08x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| nbody          | 71.3 ms                                                     | 79.6 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                       |
| regex_compile  | 106 ms                                                      | 103 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.63 ms: 1.63x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 180 us: 1.50x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 160 us: 1.15x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.50 sec: 1.12x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.42 us: 1.08x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.9 ms: 1.05x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.64 us: 1.03x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.7 us: 1.02x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 55.1 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.6 ms: 1.03x slower                                                       |
| pickle               | 6.85 us                                                     | 7.12 us: 1.04x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.4 us: 1.07x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.12 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 23.5 ms: 1.23x faster                                                       |
| mako            | 9.03 ms                                                     | 7.39 ms: 1.22x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.0 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 73.5 us: 4.57x faster                                                       |
| async_tree_none          | 435 ms                                                      | 222 ms: 1.96x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 276 ms: 1.91x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.21 ms: 1.90x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 586 ms: 1.89x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 57.2 ns: 1.66x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.7 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 387 ms: 1.65x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 5.63 ms: 1.63x faster                                                       |
| pylint                   | 350 ms                                                      | 220 ms: 1.59x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 481 ms: 1.52x faster                                                        |
| richards                 | 42.4 ms                                                     | 28.2 ms: 1.51x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 180 us: 1.50x faster                                                        |
| generators               | 32.4 ms                                                     | 21.9 ms: 1.48x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 824 us: 1.47x faster                                                        |
| raytrace                 | 273 ms                                                      | 194 ms: 1.41x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.05 ms: 1.40x faster                                                       |
| go                       | 139 ms                                                      | 101 ms: 1.38x faster                                                        |
| chaos                    | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.8 ms: 1.31x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.62 sec: 1.30x faster                                                      |
| pycparser                | 930 ms                                                      | 728 ms: 1.28x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 49.6 ms: 1.26x faster                                                       |
| tornado_http             | 108 ms                                                      | 87.1 ms: 1.24x faster                                                       |
| django_template          | 28.9 ms                                                     | 23.5 ms: 1.23x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 23.5 us: 1.22x faster                                                       |
| comprehensions           | 16.5 us                                                     | 13.5 us: 1.22x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.39 ms: 1.22x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                                       |
| pyflate                  | 409 ms                                                      | 339 ms: 1.21x faster                                                        |
| scimark_sor              | 106 ms                                                      | 89.2 ms: 1.19x faster                                                       |
| chameleon                | 5.79 ms                                                     | 4.89 ms: 1.18x faster                                                       |
| mypy2                    | 555 ms                                                      | 470 ms: 1.18x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.17x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 160 us: 1.15x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 36.0 ms: 1.14x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 843 us: 1.14x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 522 ms: 1.13x faster                                                        |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.08 sec: 1.13x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 44.8 ms: 1.13x faster                                                       |
| sympy_sum                | 107 ms                                                      | 95.2 ms: 1.12x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.2 ms: 1.12x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.50 sec: 1.12x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 78.1 ms: 1.10x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.9 ms: 1.10x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.01 us: 1.10x faster                                                       |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| deepcopy                 | 255 us                                                      | 234 us: 1.09x faster                                                        |
| json                     | 3.14 ms                                                     | 2.88 ms: 1.09x faster                                                       |
| float                    | 61.7 ms                                                     | 57.1 ms: 1.08x faster                                                       |
| aiohttp                  | 995 us                                                      | 921 us: 1.08x faster                                                        |
| unpickle                 | 9.09 us                                                     | 8.42 us: 1.08x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.9 ms: 1.08x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 191 ms: 1.08x faster                                                        |
| create_gc_cycles         | 800 us                                                      | 744 us: 1.08x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 5.35 ms: 1.07x faster                                                       |
| sympy_str                | 194 ms                                                      | 181 ms: 1.07x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 91.9 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.64 us: 1.03x faster                                                       |
| regex_compile            | 106 ms                                                      | 103 ms: 1.03x faster                                                        |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                        |
| json_loads               | 14.0 us                                                     | 13.7 us: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 55.1 ms: 1.01x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 75.6 ms: 1.00x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.86 us: 1.01x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.6 ms: 1.03x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.44 us: 1.04x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 78.6 ms: 1.04x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.12 us: 1.04x slower                                                       |
| nqueens                  | 66.6 ms                                                     | 69.5 ms: 1.04x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.48 ms: 1.05x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 65.0 ms: 1.05x slower                                                       |
| spectral_norm            | 77.3 ms                                                     | 82.7 ms: 1.07x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.4 us: 1.07x slower                                                       |
| fannkuch                 | 256 ms                                                      | 279 ms: 1.09x slower                                                        |
| async_generators         | 222 ms                                                      | 246 ms: 1.11x slower                                                        |
| nbody                    | 71.3 ms                                                     | 79.6 ms: 1.12x slower                                                       |
| scimark_fft              | 187 ms                                                      | 212 ms: 1.13x slower                                                        |
| unpack_sequence          | 39.6 ns                                                     | 44.9 ns: 1.13x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.12 us: 1.13x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.1 ms: 1.18x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.29 ms: 1.21x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.85 ms: 1.23x slower                                                       |
| thrift                   | 617 us                                                      | 9.52 ms: 15.41x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): python_startup
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240323-3.13.0a5+-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x


# Memory

- memory change: unknown