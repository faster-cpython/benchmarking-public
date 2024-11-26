# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: windows-amd64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.167x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 229 ms: 1.07x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.72 sec: 1.12x faster                                                               |
| html5lib       | 51.0 ms                                                     | 43.8 ms: 1.17x faster                                                                |
| tornado_http   | 108 ms                                                      | 94.1 ms: 1.15x faster                                                                |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 214 ms: 2.04x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 270 ms: 1.95x faster                                                                 |
| async_tree_io           | 1.11 sec                                                    | 594 ms: 1.87x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 396 ms: 1.61x faster                                                                 |
| Geometric mean          | (ref)                                                       | 1.86x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 54.1 ms: 1.14x faster                                                                |
| pidigits       | 149 ms                                                      | 148 ms: 1.00x faster                                                                 |
| nbody          | 71.3 ms                                                     | 82.9 ms: 1.16x slower                                                                |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                                 |
| regex_compile  | 106 ms                                                      | 90.8 ms: 1.17x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 14.9 ms: 1.04x faster                                                                |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.73 ms: 1.36x faster                                                                |
| pickle_pure_python   | 270 us                                                      | 217 us: 1.24x faster                                                                 |
| unpickle_pure_python | 183 us                                                      | 149 us: 1.23x faster                                                                 |
| xml_etree_process    | 44.5 ms                                                     | 41.0 ms: 1.09x faster                                                                |
| tomli_loads          | 1.67 sec                                                    | 1.65 sec: 1.01x faster                                                               |
| unpickle_list        | 2.71 us                                                     | 2.77 us: 1.02x slower                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 67.0 ms: 1.03x slower                                                                |
| unpickle             | 9.09 us                                                     | 9.47 us: 1.04x slower                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 58.0 ms: 1.04x slower                                                                |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.06x slower                                                                |
| pickle_list          | 2.75 us                                                     | 2.97 us: 1.08x slower                                                                |
| pickle               | 6.85 us                                                     | 7.45 us: 1.09x slower                                                                |
| pickle_dict          | 17.2 us                                                     | 19.3 us: 1.12x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.79 ms: 1.33x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 17.4 ms: 1.14x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 37.1 ms: 1.11x faster                                                                |
| django_template | 28.9 ms                                                     | 26.3 ms: 1.10x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.89x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 214 ms: 2.04x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 270 ms: 1.95x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 594 ms: 1.87x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.83x faster                                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 396 ms: 1.61x faster                                                                 |
| go                       | 139 ms                                                      | 86.4 ms: 1.61x faster                                                                |
| logging_silent           | 94.6 ns                                                     | 60.8 ns: 1.56x faster                                                                |
| pylint                   | 350 ms                                                      | 228 ms: 1.54x faster                                                                 |
| generators               | 32.4 ms                                                     | 21.8 ms: 1.49x faster                                                                |
| richards_super           | 52.2 ms                                                     | 35.7 ms: 1.46x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 19.9 us: 1.45x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 59.6 ms: 1.44x faster                                                                |
| raytrace                 | 273 ms                                                      | 194 ms: 1.41x faster                                                                 |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.40x faster                                                                |
| chaos                    | 61.7 ms                                                     | 44.2 ms: 1.39x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.73 ms: 1.36x faster                                                                |
| sqlglot_parse            | 1.22 ms                                                     | 894 us: 1.36x faster                                                                 |
| richards                 | 42.4 ms                                                     | 31.7 ms: 1.34x faster                                                                |
| mako                     | 9.03 ms                                                     | 6.79 ms: 1.33x faster                                                                |
| deepcopy                 | 255 us                                                      | 193 us: 1.33x faster                                                                 |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.39 ms: 1.31x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 48.1 ms: 1.30x faster                                                                |
| pyflate                  | 409 ms                                                      | 321 ms: 1.27x faster                                                                 |
| pycparser                | 930 ms                                                      | 741 ms: 1.26x faster                                                                 |
| pickle_pure_python       | 270 us                                                      | 217 us: 1.24x faster                                                                 |
| unpickle_pure_python     | 183 us                                                      | 149 us: 1.23x faster                                                                 |
| scimark_monte_carlo      | 57.3 ms                                                     | 46.6 ms: 1.23x faster                                                                |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.72 sec: 1.23x faster                                                               |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                                 |
| sympy_sum                | 107 ms                                                      | 89.8 ms: 1.19x faster                                                                |
| thrift                   | 617 us                                                      | 524 us: 1.18x faster                                                                 |
| scimark_sor              | 106 ms                                                      | 90.1 ms: 1.18x faster                                                                |
| mdp                      | 1.78 sec                                                    | 1.52 sec: 1.17x faster                                                               |
| regex_compile            | 106 ms                                                      | 90.8 ms: 1.17x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 43.8 ms: 1.17x faster                                                                |
| bench_thread_pool        | 958 us                                                      | 825 us: 1.16x faster                                                                 |
| tornado_http             | 108 ms                                                      | 94.1 ms: 1.15x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 43.9 ms: 1.15x faster                                                                |
| asyncio_tcp              | 732 ms                                                      | 641 ms: 1.14x faster                                                                 |
| genshi_text              | 19.8 ms                                                     | 17.4 ms: 1.14x faster                                                                |
| float                    | 61.7 ms                                                     | 54.1 ms: 1.14x faster                                                                |
| sqlite_synth             | 1.91 us                                                     | 1.68 us: 1.14x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 69.0 ms: 1.12x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.72 sec: 1.12x faster                                                               |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.11x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 37.1 ms: 1.11x faster                                                                |
| django_template          | 28.9 ms                                                     | 26.3 ms: 1.10x faster                                                                |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                                 |
| deepcopy_reduce          | 2.20 us                                                     | 2.02 us: 1.09x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                               |
| xml_etree_process        | 44.5 ms                                                     | 41.0 ms: 1.09x faster                                                                |
| pprint_safe_repr         | 592 ms                                                      | 547 ms: 1.08x faster                                                                 |
| 2to3                     | 246 ms                                                      | 229 ms: 1.07x faster                                                                 |
| sqlglot_optimize         | 39.8 ms                                                     | 37.1 ms: 1.07x faster                                                                |
| unpack_sequence          | 39.6 ns                                                     | 37.5 ns: 1.06x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                                |
| sqlglot_normalize        | 205 ms                                                      | 198 ms: 1.04x faster                                                                 |
| regex_v8                 | 15.4 ms                                                     | 14.9 ms: 1.04x faster                                                                |
| nqueens                  | 66.6 ms                                                     | 64.6 ms: 1.03x faster                                                                |
| sympy_expand             | 314 ms                                                      | 307 ms: 1.02x faster                                                                 |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.67 ms: 1.02x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.65 sec: 1.01x faster                                                               |
| pidigits                 | 149 ms                                                      | 148 ms: 1.00x faster                                                                 |
| logging_simple           | 6.22 us                                                     | 6.29 us: 1.01x slower                                                                |
| unpickle_list            | 2.71 us                                                     | 2.77 us: 1.02x slower                                                                |
| meteor_contest           | 75.9 ms                                                     | 77.6 ms: 1.02x slower                                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 67.0 ms: 1.03x slower                                                                |
| unpickle                 | 9.09 us                                                     | 9.47 us: 1.04x slower                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 58.0 ms: 1.04x slower                                                                |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.06x slower                                                                |
| pathlib                  | 75.7 ms                                                     | 80.6 ms: 1.07x slower                                                                |
| pickle_list              | 2.75 us                                                     | 2.97 us: 1.08x slower                                                                |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                                |
| pickle                   | 6.85 us                                                     | 7.45 us: 1.09x slower                                                                |
| scimark_fft              | 187 ms                                                      | 204 ms: 1.09x slower                                                                 |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                                |
| bench_mp_pool            | 62.0 ms                                                     | 68.7 ms: 1.11x slower                                                                |
| fannkuch                 | 256 ms                                                      | 286 ms: 1.12x slower                                                                 |
| pickle_dict              | 17.2 us                                                     | 19.3 us: 1.12x slower                                                                |
| async_generators         | 222 ms                                                      | 253 ms: 1.14x slower                                                                 |
| nbody                    | 71.3 ms                                                     | 82.9 ms: 1.16x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 939 us: 1.17x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.79 ms: 1.22x slower                                                                |
| coverage                 | 39.0 ms                                                     | 48.6 ms: 1.25x slower                                                                |
| json                     | 3.14 ms                                                     | 4.46 ms: 1.42x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                                         |

Benchmark hidden because not significant (2): xml_etree_parse, logging_format
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.167x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown