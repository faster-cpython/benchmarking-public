# Results vs. 3.10.4

- fork: python
- ref: d472b4f9fa4fb6061588
- machine: windows-amd64
- commit hash: d472b4f
- commit date: 2024-05-22
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 235 ms: 1.05x faster                                                       |
| chameleon      | 5.79 ms                                                     | 5.13 ms: 1.13x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.6 ms: 1.36x faster                                                      |
| tornado_http   | 108 ms                                                      | 86.0 ms: 1.26x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 281 ms: 1.87x faster                                                       |
| async_tree_none         | 435 ms                                                      | 232 ms: 1.87x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 610 ms: 1.82x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 403 ms: 1.58x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.78x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 51.2 ms: 1.39x faster                                                      |
| float          | 61.7 ms                                                     | 45.2 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.3 ms: 1.19x faster                                                      |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.66 ms: 1.62x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 172 us: 1.56x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 129 us: 1.42x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.8 ms: 1.09x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.7 ms: 1.07x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.57 us: 1.06x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.79 us: 1.03x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.0 us: 1.05x slower                                                      |
| pickle               | 6.85 us                                                     | 7.35 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (2): json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.03 ms: 1.80x faster                                                      |
| django_template | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.3 ms: 1.08x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 45.6 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.96x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 281 ms: 1.87x faster                                                       |
| async_tree_none          | 435 ms                                                      | 232 ms: 1.87x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 610 ms: 1.82x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.03 ms: 1.80x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.38 ms: 1.76x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 45.4 ms: 1.70x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 56.8 ns: 1.67x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.66 ms: 1.62x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.61x faster                                                      |
| pyflate                  | 409 ms                                                      | 259 ms: 1.58x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 403 ms: 1.58x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 172 us: 1.56x faster                                                       |
| chaos                    | 61.7 ms                                                     | 39.8 ms: 1.55x faster                                                      |
| raytrace                 | 273 ms                                                      | 177 ms: 1.55x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 478 ms: 1.53x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.1 ms: 1.53x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 41.1 ms: 1.52x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.1 ms: 1.51x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 813 us: 1.49x faster                                                       |
| go                       | 139 ms                                                      | 93.6 ms: 1.48x faster                                                      |
| generators               | 32.4 ms                                                     | 21.8 ms: 1.48x faster                                                      |
| pylint                   | 350 ms                                                      | 238 ms: 1.47x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.45 sec: 1.46x faster                                                     |
| richards                 | 42.4 ms                                                     | 29.9 ms: 1.42x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 129 us: 1.42x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.05 ms: 1.40x faster                                                      |
| nbody                    | 71.3 ms                                                     | 51.2 ms: 1.39x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.9 us: 1.37x faster                                                      |
| float                    | 61.7 ms                                                     | 45.2 ms: 1.36x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.6 ms: 1.36x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 941 ms: 1.30x faster                                                       |
| scimark_sor              | 106 ms                                                      | 82.4 ms: 1.29x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 460 ms: 1.29x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.13 ms: 1.28x faster                                                      |
| scimark_fft              | 187 ms                                                      | 147 ms: 1.28x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.40 sec: 1.27x faster                                                     |
| tornado_http             | 108 ms                                                      | 86.0 ms: 1.26x faster                                                      |
| pycparser                | 930 ms                                                      | 742 ms: 1.25x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.71 ms: 1.22x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                                      |
| thrift                   | 617 us                                                      | 516 us: 1.20x faster                                                       |
| regex_compile            | 106 ms                                                      | 89.3 ms: 1.19x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.18x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 73.1 ms: 1.17x faster                                                      |
| fannkuch                 | 256 ms                                                      | 218 ms: 1.17x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 849 us: 1.13x faster                                                       |
| chameleon                | 5.79 ms                                                     | 5.13 ms: 1.13x faster                                                      |
| sympy_sum                | 107 ms                                                      | 94.9 ms: 1.13x faster                                                      |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.8 ms: 1.09x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.1 ms: 1.09x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.22 us: 1.09x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.3 ms: 1.08x faster                                                      |
| sympy_str                | 194 ms                                                      | 179 ms: 1.08x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                                      |
| deepcopy                 | 255 us                                                      | 237 us: 1.08x faster                                                       |
| json                     | 3.14 ms                                                     | 2.91 ms: 1.08x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 51.7 ms: 1.07x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                                     |
| logging_simple           | 6.22 us                                                     | 5.80 us: 1.07x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.06 us: 1.07x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 37.3 ms: 1.07x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.7 ms: 1.06x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.57 us: 1.06x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.0 ms: 1.05x faster                                                      |
| 2to3                     | 246 ms                                                      | 235 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| sympy_expand             | 314 ms                                                      | 315 ms: 1.00x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.79 us: 1.03x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.0 us: 1.05x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 79.5 ms: 1.05x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.35 us: 1.07x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 45.6 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 890 us: 1.11x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 70.4 ms: 1.13x slower                                                      |
| async_generators         | 222 ms                                                      | 252 ms: 1.14x slower                                                       |
| coverage                 | 39.0 ms                                                     | 44.4 ms: 1.14x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.56 ms: 1.16x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (5): pidigits, flaskblogging, json_loads, pickle_list, regex_v8
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240522-3.14.0a0-d472b4f-JIT/bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown