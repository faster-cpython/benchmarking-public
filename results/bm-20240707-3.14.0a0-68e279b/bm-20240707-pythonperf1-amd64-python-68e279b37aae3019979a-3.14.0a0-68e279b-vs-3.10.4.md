# Results vs. 3.10.4

- fork: python
- ref: 68e279b37aae3019979a
- machine: windows-amd64
- commit hash: 68e279b
- commit date: 2024-07-07
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 214 ms: 1.15x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                     |
| html5lib       | 51.0 ms                                                     | 36.4 ms: 1.40x faster                                                      |
| tornado_http   | 108 ms                                                      | 80.9 ms: 1.34x faster                                                      |
| Geometric mean | (ref)                                                       | 1.26x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 522 ms: 2.12x faster                                                       |
| async_tree_none         | 435 ms                                                      | 205 ms: 2.12x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 250 ms: 2.11x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 380 ms: 1.68x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.00x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 52.6 ms: 1.17x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 73.2 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.5 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 17.1 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.66 ms: 1.62x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 186 us: 1.45x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 133 us: 1.38x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 37.8 ms: 1.18x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.47 sec: 1.14x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 92.4 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 55.0 ms: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.9 ms: 1.01x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 16.7 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.59 ms: 1.37x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                      |
| django_template | 28.9 ms                                                     | 23.2 ms: 1.25x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 33.1 ms: 1.24x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.29x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.31x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 522 ms: 2.12x faster                                                       |
| async_tree_none          | 435 ms                                                      | 205 ms: 2.12x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.99 ms: 2.11x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 250 ms: 2.11x faster                                                       |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.6 ms: 1.71x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 380 ms: 1.68x faster                                                       |
| raytrace                 | 273 ms                                                      | 167 ms: 1.64x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 57.9 ns: 1.63x faster                                                      |
| go                       | 139 ms                                                      | 85.7 ms: 1.62x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.66 ms: 1.62x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.9 ms: 1.57x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.2 ms: 1.57x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.56x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.6 us: 1.55x faster                                                      |
| generators               | 32.4 ms                                                     | 21.0 ms: 1.54x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 477 ms: 1.53x faster                                                       |
| deepcopy                 | 255 us                                                      | 170 us: 1.50x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 813 us: 1.49x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.90 ms: 1.47x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 186 us: 1.45x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 59.8 ms: 1.44x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.03 ms: 1.44x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 36.4 ms: 1.40x faster                                                      |
| pyflate                  | 409 ms                                                      | 293 ms: 1.40x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 133 us: 1.38x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.59 ms: 1.37x faster                                                      |
| scimark_sor              | 106 ms                                                      | 78.4 ms: 1.35x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.5 ms: 1.35x faster                                                      |
| tornado_http             | 108 ms                                                      | 80.9 ms: 1.34x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.8 ms: 1.34x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.60 sec: 1.32x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.6 ms: 1.32x faster                                                      |
| pycparser                | 930 ms                                                      | 710 ms: 1.31x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 750 us: 1.28x faster                                                       |
| sympy_sum                | 107 ms                                                      | 84.9 ms: 1.26x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.76 us: 1.25x faster                                                      |
| django_template          | 28.9 ms                                                     | 23.2 ms: 1.25x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 62.3 ms: 1.24x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 33.1 ms: 1.24x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                      |
| thrift                   | 617 us                                                      | 509 us: 1.21x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                                     |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.21x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 33.1 ms: 1.20x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 496 ms: 1.19x faster                                                       |
| sympy_str                | 194 ms                                                      | 164 ms: 1.19x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.19x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 37.8 ms: 1.18x faster                                                      |
| float                    | 61.7 ms                                                     | 52.6 ms: 1.17x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 175 ms: 1.17x faster                                                       |
| 2to3                     | 246 ms                                                      | 214 ms: 1.15x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 58.2 ms: 1.14x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.47 sec: 1.14x faster                                                     |
| sympy_expand             | 314 ms                                                      | 278 ms: 1.13x faster                                                       |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.33 us: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.07x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.89 us: 1.06x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.4 ms: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.64 ms: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| scimark_fft              | 187 ms                                                      | 185 ms: 1.01x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 74.9 ms: 1.01x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 55.0 ms: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| python_startup           | 20.6 ms                                                     | 20.9 ms: 1.01x slower                                                      |
| nbody                    | 71.3 ms                                                     | 73.2 ms: 1.03x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 65.0 ms: 1.05x slower                                                      |
| async_generators         | 222 ms                                                      | 233 ms: 1.05x slower                                                       |
| fannkuch                 | 256 ms                                                      | 273 ms: 1.07x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.7 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 17.1 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 885 us: 1.11x slower                                                       |
| coverage                 | 39.0 ms                                                     | 45.8 ms: 1.17x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.69 ms: 1.19x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (2): json_loads, pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240707-3.14.0a0-68e279b/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown