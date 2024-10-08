# Results vs. 3.10.4

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: windows-amd64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.3 ms: 1.27x faster                                                      |
| tornado_http   | 108 ms                                                      | 84.4 ms: 1.28x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 208 ms: 2.09x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 262 ms: 2.01x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 570 ms: 1.95x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.91x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.1 ms: 1.10x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                                       |
| nbody          | 71.3 ms                                                     | 83.7 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.8 ms: 1.16x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.6 ms: 1.05x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.19 ms: 1.48x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 210 us: 1.28x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 151 us: 1.21x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.1 ms: 1.08x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 93.5 ms: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.9 ms: 1.04x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.83 us: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.23 us: 1.06x slower                                                      |
| unpickle             | 9.09 us                                                     | 9.62 us: 1.06x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.5 us: 1.08x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.00 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.7 ms: 1.06x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.6 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.89 ms: 1.31x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.0 ms: 1.14x faster                                                      |
| django_template | 28.9 ms                                                     | 26.0 ms: 1.11x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.97x faster                                                       |
| async_tree_none          | 435 ms                                                      | 208 ms: 2.09x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 262 ms: 2.01x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 570 ms: 1.95x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.84x faster                                                      |
| go                       | 139 ms                                                      | 85.8 ms: 1.62x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| pylint                   | 350 ms                                                      | 224 ms: 1.56x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 474 ms: 1.55x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.38 sec: 1.53x faster                                                     |
| logging_silent           | 94.6 ns                                                     | 62.2 ns: 1.52x faster                                                      |
| generators               | 32.4 ms                                                     | 21.5 ms: 1.51x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.19 ms: 1.48x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 58.4 ms: 1.47x faster                                                      |
| richards_super           | 52.2 ms                                                     | 35.9 ms: 1.45x faster                                                      |
| chaos                    | 61.7 ms                                                     | 43.1 ms: 1.43x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.4 us: 1.41x faster                                                      |
| raytrace                 | 273 ms                                                      | 195 ms: 1.40x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.38x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 892 us: 1.36x faster                                                       |
| deepcopy                 | 255 us                                                      | 189 us: 1.35x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                      |
| richards                 | 42.4 ms                                                     | 31.9 ms: 1.33x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.37 ms: 1.31x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.89 ms: 1.31x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.8 ms: 1.31x faster                                                      |
| tornado_http             | 108 ms                                                      | 84.4 ms: 1.28x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 210 us: 1.28x faster                                                       |
| pyflate                  | 409 ms                                                      | 320 ms: 1.28x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.3 ms: 1.27x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.23x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 151 us: 1.21x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.0 ms: 1.19x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 808 us: 1.19x faster                                                       |
| pycparser                | 930 ms                                                      | 786 ms: 1.18x faster                                                       |
| thrift                   | 617 us                                                      | 523 us: 1.18x faster                                                       |
| scimark_sor              | 106 ms                                                      | 89.9 ms: 1.18x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.8 ms: 1.18x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.7 ms: 1.18x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 66.4 ms: 1.16x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.64 us: 1.16x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                                      |
| regex_compile            | 106 ms                                                      | 91.8 ms: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.93 us: 1.14x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 36.0 ms: 1.14x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| django_template          | 28.9 ms                                                     | 26.0 ms: 1.11x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 36.2 ms: 1.10x faster                                                      |
| float                    | 61.7 ms                                                     | 56.1 ms: 1.10x faster                                                      |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                       |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 541 ms: 1.09x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.1 ms: 1.08x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 193 ms: 1.06x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 63.1 ms: 1.06x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.6 ms: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.5 ms: 1.04x faster                                                      |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.69 ms: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                                       |
| logging_format           | 6.76 us                                                     | 6.91 us: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.43 us: 1.03x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 78.9 ms: 1.04x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.9 ms: 1.04x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.83 us: 1.04x slower                                                      |
| scimark_fft              | 187 ms                                                      | 196 ms: 1.05x slower                                                       |
| python_startup           | 20.6 ms                                                     | 21.7 ms: 1.06x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.23 us: 1.06x slower                                                      |
| unpickle                 | 9.09 us                                                     | 9.62 us: 1.06x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.5 us: 1.08x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 42.7 ns: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.53 ms: 1.08x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 67.6 ms: 1.09x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.00 us: 1.09x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 883 us: 1.10x slower                                                       |
| async_generators         | 222 ms                                                      | 245 ms: 1.11x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.6 ms: 1.13x slower                                                      |
| fannkuch                 | 256 ms                                                      | 294 ms: 1.15x slower                                                       |
| nbody                    | 71.3 ms                                                     | 83.7 ms: 1.17x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.9 ms: 1.20x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.97 ms: 1.26x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_iterparse, pathlib, json
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown