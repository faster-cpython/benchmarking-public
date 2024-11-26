# Results vs. 3.10.4

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: windows-amd64
- commit hash: 8504cc0
- commit date: 2024-09-30
- overall geometric mean: 1.229x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 215 ms: 1.14x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.78 ms: 1.21x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.56 sec: 1.23x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.0 ms: 1.27x faster                                                       |
| tornado_http   | 108 ms                                                      | 92.5 ms: 1.17x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 516 ms: 2.15x faster                                                        |
| async_tree_none         | 435 ms                                                      | 221 ms: 1.97x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 269 ms: 1.95x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 377 ms: 1.69x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.93x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 49.9 ms: 1.24x faster                                                       |
| nbody          | 71.3 ms                                                     | 68.5 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.6 ms: 1.30x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.71 ms: 1.61x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 180 us: 1.50x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 127 us: 1.45x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.40 sec: 1.20x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.4 ms: 1.06x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.3 ms: 1.05x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 53.7 ms: 1.03x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.64 us: 1.03x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.86 us: 1.03x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                       |
| pickle               | 6.85 us                                                     | 7.11 us: 1.04x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.3 us: 1.06x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.08 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.23 ms: 1.45x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.0 ms: 1.32x faster                                                       |
| django_template | 28.9 ms                                                     | 22.2 ms: 1.30x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 32.9 ms: 1.25x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.32x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.88 ms: 2.23x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 516 ms: 2.15x faster                                                        |
| async_tree_none          | 435 ms                                                      | 221 ms: 1.97x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 269 ms: 1.95x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 53.2 ns: 1.78x faster                                                       |
| richards_super           | 52.2 ms                                                     | 29.8 ms: 1.75x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 377 ms: 1.69x faster                                                        |
| raytrace                 | 273 ms                                                      | 163 ms: 1.68x faster                                                        |
| pylint                   | 350 ms                                                      | 210 ms: 1.67x faster                                                        |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.64x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.1 us: 1.63x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.71 ms: 1.61x faster                                                       |
| chaos                    | 61.7 ms                                                     | 38.5 ms: 1.60x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 54.0 ms: 1.59x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 769 us: 1.58x faster                                                        |
| richards                 | 42.4 ms                                                     | 26.9 ms: 1.58x faster                                                       |
| go                       | 139 ms                                                      | 88.7 ms: 1.57x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.72 ms: 1.54x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 978 us: 1.51x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 180 us: 1.50x faster                                                        |
| pyflate                  | 409 ms                                                      | 277 ms: 1.48x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.23 ms: 1.45x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 127 us: 1.45x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.1 ms: 1.43x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 44.4 ms: 1.41x faster                                                       |
| scimark_sor              | 106 ms                                                      | 75.8 ms: 1.40x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.54 sec: 1.37x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.0 ms: 1.32x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.36 sec: 1.30x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 59.4 ms: 1.30x faster                                                       |
| django_template          | 28.9 ms                                                     | 22.2 ms: 1.30x faster                                                       |
| regex_compile            | 106 ms                                                      | 81.6 ms: 1.30x faster                                                       |
| mypy2                    | 555 ms                                                      | 430 ms: 1.29x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.0 ms: 1.27x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 579 ms: 1.26x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 22.8 us: 1.26x faster                                                       |
| coroutines               | 16.0 ms                                                     | 12.7 ms: 1.26x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 32.9 ms: 1.25x faster                                                       |
| float                    | 61.7 ms                                                     | 49.9 ms: 1.24x faster                                                       |
| sympy_sum                | 107 ms                                                      | 86.6 ms: 1.24x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.0 ms: 1.23x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.56 sec: 1.23x faster                                                      |
| pycparser                | 930 ms                                                      | 756 ms: 1.23x faster                                                        |
| chameleon                | 5.79 ms                                                     | 4.78 ms: 1.21x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.20x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 494 ms: 1.20x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.40 sec: 1.20x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.19x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 175 ms: 1.18x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 33.9 ms: 1.18x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 816 us: 1.17x faster                                                        |
| tornado_http             | 108 ms                                                      | 92.5 ms: 1.17x faster                                                       |
| sympy_str                | 194 ms                                                      | 167 ms: 1.16x faster                                                        |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 57.4 ms: 1.16x faster                                                       |
| 2to3                     | 246 ms                                                      | 215 ms: 1.14x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.40 ms: 1.14x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 35.0 ns: 1.13x faster                                                       |
| deepcopy                 | 255 us                                                      | 228 us: 1.12x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.12 us: 1.10x faster                                                       |
| sympy_expand             | 314 ms                                                      | 288 ms: 1.09x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 2.02 us: 1.09x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.72 us: 1.09x faster                                                       |
| scimark_fft              | 187 ms                                                      | 173 ms: 1.08x faster                                                        |
| aiohttp                  | 995 us                                                      | 933 us: 1.07x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.4 ms: 1.06x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.3 ms: 1.05x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 72.5 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| fannkuch                 | 256 ms                                                      | 245 ms: 1.04x faster                                                        |
| nbody                    | 71.3 ms                                                     | 68.5 ms: 1.04x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 53.7 ms: 1.03x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.64 us: 1.03x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.86 us: 1.03x faster                                                       |
| async_generators         | 222 ms                                                      | 219 ms: 1.01x faster                                                        |
| flaskblogging            | 2.03 sec                                                    | 2.03 sec: 1.00x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 813 us: 1.02x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.11 us: 1.04x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.3 us: 1.06x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 80.5 ms: 1.06x slower                                                       |
| python_startup           | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 69.3 ms: 1.12x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.08 us: 1.12x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.4 ms: 1.19x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.78 ms: 1.21x slower                                                       |
| thrift                   | 617 us                                                      | 8.53 ms: 13.82x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                |

Benchmark hidden because not significant (3): json, pidigits, regex_v8
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240930-3.13.0rc2+-8504cc0/bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.229x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown