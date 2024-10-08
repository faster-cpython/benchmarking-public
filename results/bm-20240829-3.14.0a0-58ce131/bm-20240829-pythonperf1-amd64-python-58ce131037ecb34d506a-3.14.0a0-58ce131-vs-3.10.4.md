# Results vs. 3.10.4

- fork: python
- ref: 58ce131037ecb34d506a
- machine: windows-amd64
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                      |
| tornado_http   | 108 ms                                                      | 92.8 ms: 1.17x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 209 ms: 2.08x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 254 ms: 2.07x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 579 ms: 1.92x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 390 ms: 1.63x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.0 ms: 1.10x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 85.1 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                                       |
| regex_compile  | 106 ms                                                      | 89.9 ms: 1.18x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.35 ms: 1.44x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.0 ms: 1.08x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.57 sec: 1.07x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 94.7 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 58.2 ms: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.99 ms: 1.29x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                      |
| django_template | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.9 ms: 1.11x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.02x faster                                                       |
| async_tree_none          | 435 ms                                                      | 209 ms: 2.08x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 254 ms: 2.07x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 579 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.24 ms: 1.87x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 390 ms: 1.63x faster                                                       |
| go                       | 139 ms                                                      | 85.4 ms: 1.63x faster                                                      |
| pylint                   | 350 ms                                                      | 227 ms: 1.54x faster                                                       |
| generators               | 32.4 ms                                                     | 21.1 ms: 1.54x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 63.3 ns: 1.50x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.35 ms: 1.44x faster                                                      |
| raytrace                 | 273 ms                                                      | 190 ms: 1.44x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.0 ms: 1.43x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.1 us: 1.43x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.5 ms: 1.43x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.39x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 527 ms: 1.39x faster                                                       |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 879 us: 1.38x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.54 sec: 1.37x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 63.0 ms: 1.36x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.09 ms: 1.35x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.33 ms: 1.33x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.7 ms: 1.31x faster                                                      |
| richards                 | 42.4 ms                                                     | 32.4 ms: 1.31x faster                                                      |
| pyflate                  | 409 ms                                                      | 316 ms: 1.29x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.99 ms: 1.29x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.45 sec: 1.22x faster                                                     |
| thrift                   | 617 us                                                      | 510 us: 1.21x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.3 ms: 1.20x faster                                                      |
| scimark_sor              | 106 ms                                                      | 89.4 ms: 1.19x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.6 ms: 1.19x faster                                                      |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                                       |
| regex_compile            | 106 ms                                                      | 89.9 ms: 1.18x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.0 ms: 1.17x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 819 us: 1.17x faster                                                       |
| tornado_http             | 108 ms                                                      | 92.8 ms: 1.17x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.17x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 67.0 ms: 1.15x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.3 ms: 1.14x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                     |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.13x faster                                                      |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.9 ms: 1.11x faster                                                      |
| float                    | 61.7 ms                                                     | 56.0 ms: 1.10x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.2 ms: 1.10x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 544 ms: 1.09x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.0 ms: 1.08x faster                                                      |
| 2to3                     | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 191 ms: 1.07x faster                                                       |
| pycparser                | 930 ms                                                      | 870 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.57 sec: 1.07x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 62.6 ms: 1.06x faster                                                      |
| sympy_expand             | 314 ms                                                      | 301 ms: 1.04x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 94.7 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.33 us: 1.02x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 77.7 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.81 ms: 1.03x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 79.1 ms: 1.04x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 58.2 ms: 1.05x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| async_generators         | 222 ms                                                      | 238 ms: 1.07x slower                                                       |
| scimark_fft              | 187 ms                                                      | 204 ms: 1.09x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| fannkuch                 | 256 ms                                                      | 288 ms: 1.13x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 70.3 ms: 1.13x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 911 us: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                                      |
| nbody                    | 71.3 ms                                                     | 85.1 ms: 1.19x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.0 ms: 1.21x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.01 ms: 1.27x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (5): json, regex_v8, logging_format, json_loads, xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240829-3.14.0a0-58ce131/bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown