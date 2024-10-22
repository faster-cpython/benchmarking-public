# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel
- machine: windows-amd64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 234 ms: 1.05x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.78 sec: 1.08x faster                                                     |
| html5lib       | 51.0 ms                                                     | 41.9 ms: 1.22x faster                                                      |
| tornado_http   | 108 ms                                                      | 85.4 ms: 1.27x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 208 ms: 2.09x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 256 ms: 2.06x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 543 ms: 2.04x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 382 ms: 1.67x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.96x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 51.1 ms: 1.40x faster                                                      |
| float          | 61.7 ms                                                     | 45.1 ms: 1.37x faster                                                      |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.2 ms: 1.18x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 23.9 ms: 1.55x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.78 ms: 1.59x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 179 us: 1.51x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 134 us: 1.37x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 52.8 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.1 ms: 1.05x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 93.4 ms: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.9 ms: 1.01x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.18 ms: 1.74x faster                                                      |
| django_template | 28.9 ms                                                     | 26.3 ms: 1.10x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.2 ms: 1.09x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 44.8 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 2.99x faster                                                       |
| async_tree_none          | 435 ms                                                      | 208 ms: 2.09x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 256 ms: 2.06x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 543 ms: 2.04x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 15.6 us: 1.84x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.35 ms: 1.78x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.18 ms: 1.74x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 45.8 ms: 1.69x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 382 ms: 1.67x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 57.3 ns: 1.65x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.61x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.78 ms: 1.59x faster                                                      |
| pyflate                  | 409 ms                                                      | 260 ms: 1.57x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.0 ms: 1.54x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 475 ms: 1.54x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 40.8 ms: 1.53x faster                                                      |
| pylint                   | 350 ms                                                      | 232 ms: 1.51x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 179 us: 1.51x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.1 ms: 1.50x faster                                                      |
| richards_super           | 52.2 ms                                                     | 34.8 ms: 1.50x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 815 us: 1.49x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.42 sec: 1.49x faster                                                     |
| raytrace                 | 273 ms                                                      | 185 ms: 1.47x faster                                                       |
| go                       | 139 ms                                                      | 97.7 ms: 1.42x faster                                                      |
| deepcopy                 | 255 us                                                      | 180 us: 1.42x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.04 ms: 1.42x faster                                                      |
| nbody                    | 71.3 ms                                                     | 51.1 ms: 1.40x faster                                                      |
| richards                 | 42.4 ms                                                     | 30.6 ms: 1.39x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.37x faster                                                       |
| float                    | 61.7 ms                                                     | 45.1 ms: 1.37x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                     |
| generators               | 32.4 ms                                                     | 25.0 ms: 1.29x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 947 ms: 1.29x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 462 ms: 1.28x faster                                                       |
| tornado_http             | 108 ms                                                      | 85.4 ms: 1.27x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.17 ms: 1.25x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.61 ms: 1.25x faster                                                      |
| scimark_fft              | 187 ms                                                      | 151 ms: 1.24x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.23x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 41.9 ms: 1.22x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.46 sec: 1.22x faster                                                     |
| bench_thread_pool        | 958 us                                                      | 808 us: 1.18x faster                                                       |
| regex_compile            | 106 ms                                                      | 90.2 ms: 1.18x faster                                                      |
| thrift                   | 617 us                                                      | 528 us: 1.17x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                      |
| scimark_sor              | 106 ms                                                      | 91.6 ms: 1.16x faster                                                      |
| pycparser                | 930 ms                                                      | 804 ms: 1.16x faster                                                       |
| fannkuch                 | 256 ms                                                      | 225 ms: 1.14x faster                                                       |
| sympy_sum                | 107 ms                                                      | 94.0 ms: 1.14x faster                                                      |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 77.0 ms: 1.11x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.3 ms: 1.10x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.4 ms: 1.09x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.2 ms: 1.09x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.0 ms: 1.09x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.78 sec: 1.08x faster                                                     |
| logging_format           | 6.76 us                                                     | 6.27 us: 1.08x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.9 ms: 1.08x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.80 us: 1.07x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 193 ms: 1.06x faster                                                       |
| sympy_str                | 194 ms                                                      | 184 ms: 1.06x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 52.8 ms: 1.05x faster                                                      |
| 2to3                     | 246 ms                                                      | 234 ms: 1.05x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.1 ms: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.4 ms: 1.04x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 74.1 ms: 1.03x faster                                                      |
| pathlib                  | 75.7 ms                                                     | 74.9 ms: 1.01x faster                                                      |
| python_startup           | 20.6 ms                                                     | 20.9 ms: 1.01x slower                                                      |
| sympy_expand             | 314 ms                                                      | 319 ms: 1.02x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 44.8 ms: 1.09x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 69.3 ms: 1.12x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 900 us: 1.13x slower                                                       |
| async_generators         | 222 ms                                                      | 259 ms: 1.17x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.5 ms: 1.24x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.95 ms: 1.26x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 23.9 ms: 1.55x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                               |

Benchmark hidden because not significant (2): json, pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240714-3.14.0a0-d19b26c-JIT/bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown