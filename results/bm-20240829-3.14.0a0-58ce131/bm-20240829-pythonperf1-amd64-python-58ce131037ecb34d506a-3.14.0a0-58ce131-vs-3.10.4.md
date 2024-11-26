# Results vs. 3.10.4

- fork: python
- ref: 58ce131037ecb34d506a
- machine: windows-amd64
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.162x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 230 ms: 1.07x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                      |
| tornado_http   | 108 ms                                                      | 93.8 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 213 ms: 2.05x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 264 ms: 1.99x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 582 ms: 1.90x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 389 ms: 1.64x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.89x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 57.0 ms: 1.08x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 89.2 ms: 1.25x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.2 ms: 1.16x faster                                                      |
| regex_dna      | 136 ms                                                      | 124 ms: 1.10x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.64 ms: 1.01x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 15.6 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 217 us: 1.24x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 155 us: 1.18x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.9 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 94.4 ms: 1.03x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.65 sec: 1.01x faster                                                     |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.8 ms: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.02x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 59.5 ms: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.17 ms: 1.26x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                      |
| django_template | 28.9 ms                                                     | 25.0 ms: 1.15x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.4 ms: 1.13x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.05x faster                                                       |
| async_tree_none          | 435 ms                                                      | 213 ms: 2.05x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 264 ms: 1.99x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 582 ms: 1.90x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.30 ms: 1.82x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 389 ms: 1.64x faster                                                       |
| go                       | 139 ms                                                      | 87.6 ms: 1.59x faster                                                      |
| generators               | 32.4 ms                                                     | 20.7 ms: 1.57x faster                                                      |
| pylint                   | 350 ms                                                      | 228 ms: 1.54x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 64.4 ns: 1.47x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                      |
| raytrace                 | 273 ms                                                      | 189 ms: 1.45x faster                                                       |
| richards_super           | 52.2 ms                                                     | 36.9 ms: 1.42x faster                                                      |
| chaos                    | 61.7 ms                                                     | 44.2 ms: 1.40x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 538 ms: 1.36x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.2 us: 1.35x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.3 us: 1.35x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 913 us: 1.33x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.59 sec: 1.33x faster                                                     |
| deepcopy                 | 255 us                                                      | 192 us: 1.33x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 64.6 ms: 1.33x faster                                                      |
| richards                 | 42.4 ms                                                     | 32.6 ms: 1.30x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.14 ms: 1.30x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.53 ms: 1.27x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 49.6 ms: 1.26x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.17 ms: 1.26x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 217 us: 1.24x faster                                                       |
| pyflate                  | 409 ms                                                      | 329 ms: 1.24x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.19x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 155 us: 1.18x faster                                                       |
| thrift                   | 617 us                                                      | 522 us: 1.18x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.1 ms: 1.17x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 819 us: 1.17x faster                                                       |
| regex_compile            | 106 ms                                                      | 91.2 ms: 1.16x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 43.5 ms: 1.16x faster                                                      |
| tornado_http             | 108 ms                                                      | 93.8 ms: 1.16x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.0 ms: 1.15x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                      |
| pycparser                | 930 ms                                                      | 824 ms: 1.13x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.4 ms: 1.13x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                                      |
| scimark_sor              | 106 ms                                                      | 95.7 ms: 1.11x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 69.9 ms: 1.10x faster                                                      |
| regex_dna                | 136 ms                                                      | 124 ms: 1.10x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 52.4 ms: 1.09x faster                                                      |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                       |
| float                    | 61.7 ms                                                     | 57.0 ms: 1.08x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 37.0 ms: 1.07x faster                                                      |
| 2to3                     | 246 ms                                                      | 230 ms: 1.07x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.9 ms: 1.06x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.15 sec: 1.06x faster                                                     |
| sqlglot_normalize        | 205 ms                                                      | 195 ms: 1.05x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 562 ms: 1.05x faster                                                       |
| json                     | 3.14 ms                                                     | 3.02 ms: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 94.4 ms: 1.03x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.65 sec: 1.01x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 65.8 ms: 1.01x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.64 ms: 1.01x faster                                                      |
| sympy_expand             | 314 ms                                                      | 311 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.6 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.8 ms: 1.01x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.34 us: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.02x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 78.3 ms: 1.03x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 79.2 ms: 1.05x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.89 ms: 1.06x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 59.5 ms: 1.07x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| async_generators         | 222 ms                                                      | 247 ms: 1.11x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.11x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 69.2 ms: 1.12x slower                                                      |
| scimark_fft              | 187 ms                                                      | 214 ms: 1.14x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 913 us: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                      |
| fannkuch                 | 256 ms                                                      | 303 ms: 1.18x slower                                                       |
| nbody                    | 71.3 ms                                                     | 89.2 ms: 1.25x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.4 ms: 1.27x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.14 ms: 1.31x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (1): logging_format
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240829-3.14.0a0-58ce131/bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.162x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown