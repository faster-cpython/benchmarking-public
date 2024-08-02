# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-amd64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 208 ms: 1.18x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.74 ms: 1.22x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                      |
| html5lib       | 51.0 ms                                                     | 35.6 ms: 1.43x faster                                                       |
| tornado_http   | 108 ms                                                      | 82.3 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 217 ms: 2.01x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 263 ms: 2.00x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 584 ms: 1.90x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 385 ms: 1.65x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.88x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 50.2 ms: 1.23x faster                                                       |
| nbody          | 71.3 ms                                                     | 69.4 ms: 1.03x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.2 ms: 1.36x faster                                                       |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.68 ms: 1.61x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 178 us: 1.52x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 124 us: 1.48x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.42 us: 1.08x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.9 ms: 1.05x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.59 us: 1.05x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 53.5 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.9 us: 1.01x faster                                                       |
| pickle_list          | 2.75 us                                                     | 2.92 us: 1.06x slower                                                       |
| pickle               | 6.85 us                                                     | 7.32 us: 1.07x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.7 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.1 ms: 1.02x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.1 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.40 ms: 1.41x faster                                                       |
| django_template | 28.9 ms                                                     | 21.2 ms: 1.36x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 14.7 ms: 1.35x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 31.7 ms: 1.29x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.34x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.90 ms: 2.20x faster                                                       |
| async_tree_none          | 435 ms                                                      | 217 ms: 2.01x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 263 ms: 2.00x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 584 ms: 1.90x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 53.0 ns: 1.79x faster                                                       |
| pylint                   | 350 ms                                                      | 204 ms: 1.72x faster                                                        |
| raytrace                 | 273 ms                                                      | 161 ms: 1.70x faster                                                        |
| richards_super           | 52.2 ms                                                     | 31.0 ms: 1.69x faster                                                       |
| go                       | 139 ms                                                      | 82.7 ms: 1.68x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 385 ms: 1.65x faster                                                        |
| generators               | 32.4 ms                                                     | 19.9 ms: 1.62x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.62x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 53.0 ms: 1.62x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.68 ms: 1.61x faster                                                       |
| chaos                    | 61.7 ms                                                     | 38.4 ms: 1.61x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 757 us: 1.61x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 472 ms: 1.55x faster                                                        |
| richards                 | 42.4 ms                                                     | 27.5 ms: 1.54x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.75 ms: 1.53x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 970 us: 1.52x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 178 us: 1.52x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 124 us: 1.48x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.43 sec: 1.47x faster                                                      |
| pyflate                  | 409 ms                                                      | 279 ms: 1.47x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.9 ms: 1.43x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 35.6 ms: 1.43x faster                                                       |
| scimark_sor              | 106 ms                                                      | 74.6 ms: 1.42x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.40 ms: 1.41x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 45.5 ms: 1.38x faster                                                       |
| django_template          | 28.9 ms                                                     | 21.2 ms: 1.36x faster                                                       |
| regex_compile            | 106 ms                                                      | 78.2 ms: 1.36x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.31 sec: 1.35x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 14.7 ms: 1.35x faster                                                       |
| mypy2                    | 555 ms                                                      | 415 ms: 1.34x faster                                                        |
| tornado_http             | 108 ms                                                      | 82.3 ms: 1.32x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 38.5 ms: 1.31x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 31.7 ms: 1.29x faster                                                       |
| pycparser                | 930 ms                                                      | 721 ms: 1.29x faster                                                        |
| sympy_sum                | 107 ms                                                      | 84.0 ms: 1.27x faster                                                       |
| coroutines               | 16.0 ms                                                     | 12.7 ms: 1.26x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 22.9 us: 1.25x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.2 ms: 1.25x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 62.1 ms: 1.24x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 981 ms: 1.24x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 481 ms: 1.23x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                      |
| float                    | 61.7 ms                                                     | 50.2 ms: 1.23x faster                                                       |
| chameleon                | 5.79 ms                                                     | 4.74 ms: 1.22x faster                                                       |
| sympy_str                | 194 ms                                                      | 159 ms: 1.22x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 32.7 ms: 1.22x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 171 ms: 1.20x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 798 us: 1.20x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 55.9 ms: 1.19x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.19x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                      |
| 2to3                     | 246 ms                                                      | 208 ms: 1.18x faster                                                        |
| sympy_expand             | 314 ms                                                      | 270 ms: 1.16x faster                                                        |
| deepcopy                 | 255 us                                                      | 222 us: 1.15x faster                                                        |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.97 us: 1.12x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.45 ms: 1.11x faster                                                       |
| aiohttp                  | 995 us                                                      | 894 us: 1.11x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.13 us: 1.10x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.70 us: 1.09x faster                                                       |
| scimark_fft              | 187 ms                                                      | 173 ms: 1.08x faster                                                        |
| unpickle                 | 9.09 us                                                     | 8.42 us: 1.08x faster                                                       |
| json                     | 3.14 ms                                                     | 2.91 ms: 1.08x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 72.0 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 91.9 ms: 1.05x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.59 us: 1.05x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 53.5 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| nbody                    | 71.3 ms                                                     | 69.4 ms: 1.03x faster                                                       |
| fannkuch                 | 256 ms                                                      | 249 ms: 1.03x faster                                                        |
| python_startup           | 20.6 ms                                                     | 20.1 ms: 1.02x faster                                                       |
| json_loads               | 14.0 us                                                     | 13.9 us: 1.01x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 74.8 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 16.1 ms: 1.04x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 65.0 ms: 1.05x slower                                                       |
| pickle_list              | 2.75 us                                                     | 2.92 us: 1.06x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.32 us: 1.07x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.7 us: 1.09x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.10x slower                                                       |
| coverage                 | 39.0 ms                                                     | 43.7 ms: 1.12x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 909 us: 1.14x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.71 ms: 1.20x slower                                                       |
| thrift                   | 617 us                                                      | 8.02 ms: 12.99x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                |

Benchmark hidden because not significant (2): flaskblogging, regex_v8
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown