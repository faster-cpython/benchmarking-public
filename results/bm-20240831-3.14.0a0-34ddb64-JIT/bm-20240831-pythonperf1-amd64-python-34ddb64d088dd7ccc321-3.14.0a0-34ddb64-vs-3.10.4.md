# Results vs. 3.10.4

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-amd64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 243 ms: 1.01x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.94 sec: 1.01x slower                                                     |
| html5lib       | 51.0 ms                                                     | 42.8 ms: 1.19x faster                                                      |
| tornado_http   | 108 ms                                                      | 99.1 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 206 ms: 2.12x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 251 ms: 2.09x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 586 ms: 1.89x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 395 ms: 1.61x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 50.0 ms: 1.43x faster                                                      |
| float          | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                       | 1.25x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 95.6 ms: 1.11x faster                                                      |
| regex_dna      | 136 ms                                                      | 124 ms: 1.10x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.78 ms: 1.59x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 195 us: 1.38x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.27 sec: 1.31x faster                                                     |
| unpickle_pure_python | 183 us                                                      | 145 us: 1.26x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.8 ms: 1.24x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.5 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.7 ms: 1.05x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 94.0 ms: 1.03x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.26 ms: 1.72x faster                                                      |
| django_template | 28.9 ms                                                     | 26.8 ms: 1.08x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 46.3 ms: 1.13x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.02x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.82 ms: 2.30x faster                                                      |
| async_tree_none          | 435 ms                                                      | 206 ms: 2.12x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 251 ms: 2.09x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 15.0 us: 1.92x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 586 ms: 1.89x faster                                                       |
| scimark_sor              | 106 ms                                                      | 60.5 ms: 1.75x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 44.1 ms: 1.75x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.26 ms: 1.72x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 57.3 ns: 1.65x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 38.2 ms: 1.64x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 395 ms: 1.61x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 54.0 ms: 1.59x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.78 ms: 1.59x faster                                                      |
| pyflate                  | 409 ms                                                      | 262 ms: 1.56x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.8 us: 1.53x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.7 ms: 1.52x faster                                                      |
| go                       | 139 ms                                                      | 92.0 ms: 1.51x faster                                                      |
| generators               | 32.4 ms                                                     | 21.7 ms: 1.49x faster                                                      |
| nbody                    | 71.3 ms                                                     | 50.0 ms: 1.43x faster                                                      |
| deepcopy                 | 255 us                                                      | 183 us: 1.40x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 195 us: 1.38x faster                                                       |
| raytrace                 | 273 ms                                                      | 198 ms: 1.38x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 530 ms: 1.38x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.53 sec: 1.38x faster                                                     |
| float                    | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 901 us: 1.35x faster                                                       |
| richards_super           | 52.2 ms                                                     | 39.3 ms: 1.33x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.5 ms: 1.32x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.27 sec: 1.31x faster                                                     |
| pylint                   | 350 ms                                                      | 269 ms: 1.30x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 145 us: 1.26x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.17 ms: 1.26x faster                                                      |
| scimark_fft              | 187 ms                                                      | 149 ms: 1.26x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.18 ms: 1.25x faster                                                      |
| pycparser                | 930 ms                                                      | 750 ms: 1.24x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.8 ms: 1.24x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.46 sec: 1.22x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 42.8 ms: 1.19x faster                                                      |
| thrift                   | 617 us                                                      | 519 us: 1.19x faster                                                       |
| richards                 | 42.4 ms                                                     | 36.0 ms: 1.18x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.87 ms: 1.18x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 507 ms: 1.17x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.05 sec: 1.17x faster                                                     |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 827 us: 1.16x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 44.0 ms: 1.15x faster                                                      |
| regex_compile            | 106 ms                                                      | 95.6 ms: 1.11x faster                                                      |
| regex_dna                | 136 ms                                                      | 124 ms: 1.10x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.5 ms: 1.10x faster                                                      |
| tornado_http             | 108 ms                                                      | 99.1 ms: 1.09x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.4 ms: 1.08x faster                                                      |
| sympy_sum                | 107 ms                                                      | 99.3 ms: 1.08x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.8 ms: 1.08x faster                                                      |
| fannkuch                 | 256 ms                                                      | 239 ms: 1.07x faster                                                       |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.7 ms: 1.05x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.56 us: 1.03x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 94.0 ms: 1.03x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.05 us: 1.03x faster                                                      |
| sympy_str                | 194 ms                                                      | 190 ms: 1.03x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 15.0 ms: 1.02x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 74.6 ms: 1.02x faster                                                      |
| 2to3                     | 246 ms                                                      | 243 ms: 1.01x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 203 ms: 1.01x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 40.0 ms: 1.01x slower                                                      |
| docutils                 | 1.92 sec                                                    | 1.94 sec: 1.01x slower                                                     |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| sympy_expand             | 314 ms                                                      | 329 ms: 1.05x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 79.1 ms: 1.05x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.58 ms: 1.12x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 46.3 ms: 1.13x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.58 ms: 1.16x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 933 us: 1.17x slower                                                       |
| async_generators         | 222 ms                                                      | 261 ms: 1.18x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 74.4 ms: 1.20x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.6 ms: 1.22x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (2): genshi_text, pidigits
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown