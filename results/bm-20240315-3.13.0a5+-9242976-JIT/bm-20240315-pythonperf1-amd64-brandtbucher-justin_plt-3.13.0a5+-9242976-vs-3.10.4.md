# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_plt
- machine: windows-amd64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                    |
| chameleon      | 5.79 ms                                                     | 4.71 ms: 1.23x faster                                                   |
| docutils       | 1.92 sec                                                    | 1.58 sec: 1.22x faster                                                  |
| html5lib       | 51.0 ms                                                     | 36.0 ms: 1.42x faster                                                   |
| tornado_http   | 108 ms                                                      | 83.9 ms: 1.29x faster                                                   |
| Geometric mean | (ref)                                                       | 1.25x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 262 ms: 1.66x faster                                                    |
| async_tree_memoization  | 526 ms                                                      | 336 ms: 1.57x faster                                                    |
| async_tree_io           | 1.11 sec                                                    | 714 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed | 638 ms                                                      | 451 ms: 1.41x faster                                                    |
| Geometric mean          | (ref)                                                       | 1.55x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.3 ms: 1.28x faster                                                   |
| nbody          | 71.3 ms                                                     | 57.3 ms: 1.24x faster                                                   |
| Geometric mean | (ref)                                                       | 1.17x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.3 ms: 1.29x faster                                                   |
| regex_dna      | 136 ms                                                      | 125 ms: 1.09x faster                                                    |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                   |
| regex_v8       | 15.4 ms                                                     | 17.2 ms: 1.12x slower                                                   |
| Geometric mean | (ref)                                                       | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.48 ms: 1.67x faster                                                   |
| pickle_pure_python   | 270 us                                                      | 174 us: 1.55x faster                                                    |
| unpickle_pure_python | 183 us                                                      | 125 us: 1.47x faster                                                    |
| tomli_loads          | 1.67 sec                                                    | 1.19 sec: 1.41x faster                                                  |
| xml_etree_process    | 44.5 ms                                                     | 36.9 ms: 1.20x faster                                                   |
| unpickle             | 9.09 us                                                     | 8.57 us: 1.06x faster                                                   |
| xml_etree_generate   | 55.5 ms                                                     | 53.3 ms: 1.04x faster                                                   |
| xml_etree_parse      | 96.8 ms                                                     | 93.7 ms: 1.03x faster                                                   |
| json_loads           | 14.0 us                                                     | 13.6 us: 1.03x faster                                                   |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                   |
| unpickle_list        | 2.71 us                                                     | 2.76 us: 1.02x slower                                                   |
| pickle_dict          | 17.2 us                                                     | 17.5 us: 1.02x slower                                                   |
| pickle               | 6.85 us                                                     | 7.25 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 23.1 ms: 1.12x slower                                                   |
| python_startup_no_site | 15.5 ms                                                     | 21.0 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.52 ms: 1.64x faster                                                   |
| django_template | 28.9 ms                                                     | 21.8 ms: 1.32x faster                                                   |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                   |
| genshi_xml      | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                   |
| Geometric mean  | (ref)                                                       | 1.34x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 68.2 us: 4.92x faster                                                   |
| deltablue                | 4.19 ms                                                     | 2.00 ms: 2.09x faster                                                   |
| logging_silent           | 94.6 ns                                                     | 53.2 ns: 1.78x faster                                                   |
| richards_super           | 52.2 ms                                                     | 30.6 ms: 1.71x faster                                                   |
| pylint                   | 350 ms                                                      | 207 ms: 1.69x faster                                                    |
| json_dumps               | 9.16 ms                                                     | 5.48 ms: 1.67x faster                                                   |
| async_tree_none          | 435 ms                                                      | 262 ms: 1.66x faster                                                    |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.65x faster                                                   |
| mako                     | 9.03 ms                                                     | 5.52 ms: 1.64x faster                                                   |
| sqlglot_parse            | 1.22 ms                                                     | 761 us: 1.60x faster                                                    |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.59x faster                                                   |
| async_tree_memoization   | 526 ms                                                      | 336 ms: 1.57x faster                                                    |
| pickle_pure_python       | 270 us                                                      | 174 us: 1.55x faster                                                    |
| async_tree_io            | 1.11 sec                                                    | 714 ms: 1.55x faster                                                    |
| asyncio_tcp              | 732 ms                                                      | 472 ms: 1.55x faster                                                    |
| chaos                    | 61.7 ms                                                     | 39.8 ms: 1.55x faster                                                   |
| richards                 | 42.4 ms                                                     | 27.4 ms: 1.55x faster                                                   |
| raytrace                 | 273 ms                                                      | 178 ms: 1.53x faster                                                    |
| sqlglot_transpile        | 1.48 ms                                                     | 981 us: 1.50x faster                                                    |
| spectral_norm            | 77.3 ms                                                     | 51.5 ms: 1.50x faster                                                   |
| go                       | 139 ms                                                      | 94.1 ms: 1.48x faster                                                   |
| pyflate                  | 409 ms                                                      | 277 ms: 1.48x faster                                                    |
| unpickle_pure_python     | 183 us                                                      | 125 us: 1.47x faster                                                    |
| crypto_pyaes             | 62.5 ms                                                     | 43.5 ms: 1.44x faster                                                   |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.1 ms: 1.43x faster                                                   |
| html5lib                 | 51.0 ms                                                     | 36.0 ms: 1.42x faster                                                   |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 451 ms: 1.41x faster                                                    |
| tomli_loads              | 1.67 sec                                                    | 1.19 sec: 1.41x faster                                                  |
| pycparser                | 930 ms                                                      | 669 ms: 1.39x faster                                                    |
| hexiom                   | 5.74 ms                                                     | 4.29 ms: 1.34x faster                                                   |
| deepcopy_memo            | 28.8 us                                                     | 21.6 us: 1.33x faster                                                   |
| django_template          | 28.9 ms                                                     | 21.8 ms: 1.32x faster                                                   |
| scimark_sor              | 106 ms                                                      | 81.0 ms: 1.31x faster                                                   |
| tornado_http             | 108 ms                                                      | 83.9 ms: 1.29x faster                                                   |
| regex_compile            | 106 ms                                                      | 82.3 ms: 1.29x faster                                                   |
| pprint_pformat           | 1.22 sec                                                    | 948 ms: 1.29x faster                                                    |
| mypy2                    | 555 ms                                                      | 435 ms: 1.28x faster                                                    |
| float                    | 61.7 ms                                                     | 48.3 ms: 1.28x faster                                                   |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                   |
| pprint_safe_repr         | 592 ms                                                      | 467 ms: 1.27x faster                                                    |
| sympy_sum                | 107 ms                                                      | 85.7 ms: 1.25x faster                                                   |
| nbody                    | 71.3 ms                                                     | 57.3 ms: 1.24x faster                                                   |
| coroutines               | 16.0 ms                                                     | 12.9 ms: 1.24x faster                                                   |
| chameleon                | 5.79 ms                                                     | 4.71 ms: 1.23x faster                                                   |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                   |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.24 ms: 1.22x faster                                                   |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.73 sec: 1.22x faster                                                  |
| docutils                 | 1.92 sec                                                    | 1.58 sec: 1.22x faster                                                  |
| dulwich_log              | 50.5 ms                                                     | 41.6 ms: 1.21x faster                                                   |
| fannkuch                 | 256 ms                                                      | 212 ms: 1.20x faster                                                    |
| xml_etree_process        | 44.5 ms                                                     | 36.9 ms: 1.20x faster                                                   |
| sympy_str                | 194 ms                                                      | 162 ms: 1.20x faster                                                    |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.19x faster                                                  |
| sqlglot_normalize        | 205 ms                                                      | 172 ms: 1.19x faster                                                    |
| scimark_lu               | 85.8 ms                                                     | 72.2 ms: 1.19x faster                                                   |
| genshi_xml               | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                   |
| sympy_integrate          | 15.3 ms                                                     | 12.9 ms: 1.18x faster                                                   |
| sqlglot_optimize         | 39.8 ms                                                     | 33.9 ms: 1.17x faster                                                   |
| deepcopy                 | 255 us                                                      | 219 us: 1.17x faster                                                    |
| bench_thread_pool        | 958 us                                                      | 837 us: 1.14x faster                                                    |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.14x faster                                                   |
| sympy_expand             | 314 ms                                                      | 278 ms: 1.13x faster                                                    |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                    |
| scimark_fft              | 187 ms                                                      | 169 ms: 1.11x faster                                                    |
| aiohttp                  | 995 us                                                      | 897 us: 1.11x faster                                                    |
| nqueens                  | 66.6 ms                                                     | 60.3 ms: 1.11x faster                                                   |
| regex_dna                | 136 ms                                                      | 125 ms: 1.09x faster                                                    |
| create_gc_cycles         | 800 us                                                      | 748 us: 1.07x faster                                                    |
| logging_format           | 6.76 us                                                     | 6.33 us: 1.07x faster                                                   |
| unpickle                 | 9.09 us                                                     | 8.57 us: 1.06x faster                                                   |
| logging_simple           | 6.22 us                                                     | 5.89 us: 1.06x faster                                                   |
| meteor_contest           | 75.9 ms                                                     | 72.7 ms: 1.04x faster                                                   |
| xml_etree_generate       | 55.5 ms                                                     | 53.3 ms: 1.04x faster                                                   |
| xml_etree_parse          | 96.8 ms                                                     | 93.7 ms: 1.03x faster                                                   |
| json_loads               | 14.0 us                                                     | 13.6 us: 1.03x faster                                                   |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                   |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                   |
| pathlib                  | 75.7 ms                                                     | 76.6 ms: 1.01x slower                                                   |
| unpickle_list            | 2.71 us                                                     | 2.76 us: 1.02x slower                                                   |
| pickle_dict              | 17.2 us                                                     | 17.5 us: 1.02x slower                                                   |
| pickle                   | 6.85 us                                                     | 7.25 us: 1.06x slower                                                   |
| async_generators         | 222 ms                                                      | 236 ms: 1.07x slower                                                    |
| gc_traversal             | 1.41 ms                                                     | 1.53 ms: 1.09x slower                                                   |
| bench_mp_pool            | 62.0 ms                                                     | 69.0 ms: 1.11x slower                                                   |
| regex_v8                 | 15.4 ms                                                     | 17.2 ms: 1.12x slower                                                   |
| python_startup           | 20.6 ms                                                     | 23.1 ms: 1.12x slower                                                   |
| telco                    | 3.94 ms                                                     | 4.70 ms: 1.19x slower                                                   |
| coverage                 | 39.0 ms                                                     | 47.3 ms: 1.21x slower                                                   |
| unpack_sequence          | 39.6 ns                                                     | 49.1 ns: 1.24x slower                                                   |
| python_startup_no_site   | 15.5 ms                                                     | 21.0 ms: 1.36x slower                                                   |
| thrift                   | 617 us                                                      | 9.08 ms: 14.70x slower                                                  |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                            |

Benchmark hidden because not significant (3): json, pidigits, pickle_list
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240315-3.13.0a5+-9242976-JIT/bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x


# Memory

- memory change: unknown