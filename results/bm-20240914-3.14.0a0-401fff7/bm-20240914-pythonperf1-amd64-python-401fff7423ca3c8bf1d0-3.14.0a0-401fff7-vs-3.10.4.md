# Results vs. 3.10.4

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-amd64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                      |
| tornado_http   | 108 ms                                                      | 83.5 ms: 1.30x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 211 ms: 2.06x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 263 ms: 2.00x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 576 ms: 1.92x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 386 ms: 1.65x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.90x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.9 ms: 1.10x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 83.3 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 92.3 ms: 1.15x faster                                                      |
| regex_dna      | 136 ms                                                      | 124 ms: 1.10x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 15.2 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 216 us: 1.25x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 157 us: 1.16x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.5 ms: 1.07x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 93.2 ms: 1.04x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.63 sec: 1.03x faster                                                     |
| pickle               | 6.85 us                                                     | 6.99 us: 1.02x slower                                                      |
| unpickle             | 9.09 us                                                     | 9.27 us: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.77 us: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.88 us: 1.05x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 59.0 ms: 1.06x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.5 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.82 ms: 1.32x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.8 ms: 1.11x faster                                                      |
| django_template | 28.9 ms                                                     | 26.0 ms: 1.11x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.92x faster                                                       |
| async_tree_none          | 435 ms                                                      | 211 ms: 2.06x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 263 ms: 2.00x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 576 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.83x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 386 ms: 1.65x faster                                                       |
| go                       | 139 ms                                                      | 87.8 ms: 1.58x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 469 ms: 1.56x faster                                                       |
| pylint                   | 350 ms                                                      | 225 ms: 1.56x faster                                                       |
| generators               | 32.4 ms                                                     | 20.9 ms: 1.55x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 64.8 ns: 1.46x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.7 ms: 1.42x faster                                                      |
| chaos                    | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                      |
| raytrace                 | 273 ms                                                      | 195 ms: 1.40x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.0 us: 1.37x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 62.9 ms: 1.36x faster                                                      |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.2 us: 1.35x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 905 us: 1.34x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.82 ms: 1.32x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.13 ms: 1.31x faster                                                      |
| richards                 | 42.4 ms                                                     | 32.4 ms: 1.31x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.61 sec: 1.31x faster                                                     |
| crypto_pyaes             | 62.5 ms                                                     | 47.9 ms: 1.31x faster                                                      |
| tornado_http             | 108 ms                                                      | 83.5 ms: 1.30x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                      |
| pyflate                  | 409 ms                                                      | 326 ms: 1.26x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.57 ms: 1.26x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 216 us: 1.25x faster                                                       |
| thrift                   | 617 us                                                      | 513 us: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.3 ms: 1.19x faster                                                      |
| sympy_sum                | 107 ms                                                      | 89.7 ms: 1.19x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 813 us: 1.18x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.17x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.53 sec: 1.16x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 157 us: 1.16x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                      |
| regex_compile            | 106 ms                                                      | 92.3 ms: 1.15x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.2 ms: 1.14x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.93 us: 1.14x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| scimark_sor              | 106 ms                                                      | 93.9 ms: 1.13x faster                                                      |
| pycparser                | 930 ms                                                      | 826 ms: 1.13x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.8 ms: 1.11x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.0 ms: 1.11x faster                                                      |
| float                    | 61.7 ms                                                     | 55.9 ms: 1.10x faster                                                      |
| regex_dna                | 136 ms                                                      | 124 ms: 1.10x faster                                                       |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                       |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.5 ms: 1.09x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.13 sec: 1.08x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 551 ms: 1.07x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.5 ms: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 195 ms: 1.05x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 73.6 ms: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.2 ms: 1.04x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 64.5 ms: 1.03x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.63 sec: 1.03x faster                                                     |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.2 ms: 1.02x faster                                                      |
| pathlib                  | 75.7 ms                                                     | 74.6 ms: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.31 us: 1.01x slower                                                      |
| pickle                   | 6.85 us                                                     | 6.99 us: 1.02x slower                                                      |
| unpickle                 | 9.09 us                                                     | 9.27 us: 1.02x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.90 us: 1.02x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.77 us: 1.02x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.79 ms: 1.02x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 78.0 ms: 1.03x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.88 us: 1.05x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 59.0 ms: 1.06x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 42.2 ns: 1.06x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 66.2 ms: 1.07x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.5 us: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.52 ms: 1.08x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 874 us: 1.09x slower                                                       |
| async_generators         | 222 ms                                                      | 243 ms: 1.10x slower                                                       |
| scimark_fft              | 187 ms                                                      | 206 ms: 1.10x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                      |
| nbody                    | 71.3 ms                                                     | 83.3 ms: 1.17x slower                                                      |
| fannkuch                 | 256 ms                                                      | 302 ms: 1.18x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.8 ms: 1.23x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.01 ms: 1.27x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown