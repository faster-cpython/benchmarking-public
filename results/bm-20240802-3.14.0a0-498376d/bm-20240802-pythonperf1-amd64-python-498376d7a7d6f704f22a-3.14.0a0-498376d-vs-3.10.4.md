# Results vs. 3.10.4

- fork: python
- ref: 498376d7a7d6f704f22a
- machine: windows-amd64
- commit hash: 498376d
- commit date: 2024-08-02
- overall geometric mean: 1.14x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 232 ms: 1.06x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                                     |
| html5lib       | 51.0 ms                                                     | 42.3 ms: 1.21x faster                                                      |
| tornado_http   | 108 ms                                                      | 95.3 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 272 ms: 1.94x faster                                                       |
| async_tree_none         | 435 ms                                                      | 225 ms: 1.93x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 599 ms: 1.85x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 397 ms: 1.61x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.83x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.3 ms: 1.11x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.02x slower                                                       |
| nbody          | 71.3 ms                                                     | 91.2 ms: 1.28x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 94.2 ms: 1.13x faster                                                      |
| regex_dna      | 136 ms                                                      | 125 ms: 1.09x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.01x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 16.7 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 152 us: 1.20x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 226 us: 1.19x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 42.5 ms: 1.05x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 95.6 ms: 1.01x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.66 sec: 1.01x faster                                                     |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.2 ms: 1.02x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 59.1 ms: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.13 ms: 1.27x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.9 ms: 1.11x faster                                                      |
| django_template | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.0 ms: 1.10x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 117 us: 2.87x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 272 ms: 1.94x faster                                                       |
| async_tree_none          | 435 ms                                                      | 225 ms: 1.93x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 599 ms: 1.85x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.35 ms: 1.78x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 397 ms: 1.61x faster                                                       |
| generators               | 32.4 ms                                                     | 20.9 ms: 1.55x faster                                                      |
| pylint                   | 350 ms                                                      | 234 ms: 1.50x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 66.1 ns: 1.43x faster                                                      |
| go                       | 139 ms                                                      | 101 ms: 1.38x faster                                                       |
| richards_super           | 52.2 ms                                                     | 38.5 ms: 1.36x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.3 us: 1.35x faster                                                      |
| chaos                    | 61.7 ms                                                     | 45.8 ms: 1.35x faster                                                      |
| raytrace                 | 273 ms                                                      | 204 ms: 1.34x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 915 us: 1.33x faster                                                       |
| deepcopy                 | 255 us                                                      | 193 us: 1.32x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.5 us: 1.32x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 65.1 ms: 1.32x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.14 ms: 1.30x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.13 ms: 1.27x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.70 sec: 1.24x faster                                                     |
| richards                 | 42.4 ms                                                     | 34.2 ms: 1.24x faster                                                      |
| pyflate                  | 409 ms                                                      | 333 ms: 1.23x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.72 ms: 1.22x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 42.3 ms: 1.21x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 51.9 ms: 1.20x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 152 us: 1.20x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 226 us: 1.19x faster                                                       |
| thrift                   | 617 us                                                      | 526 us: 1.17x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 831 us: 1.15x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                      |
| sympy_sum                | 107 ms                                                      | 94.0 ms: 1.14x faster                                                      |
| tornado_http             | 108 ms                                                      | 95.3 ms: 1.14x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 44.4 ms: 1.14x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 645 ms: 1.14x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.58 sec: 1.13x faster                                                     |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.13x faster                                                      |
| regex_compile            | 106 ms                                                      | 94.2 ms: 1.13x faster                                                      |
| float                    | 61.7 ms                                                     | 55.3 ms: 1.11x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 36.9 ms: 1.11x faster                                                      |
| scimark_sor              | 106 ms                                                      | 96.2 ms: 1.10x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.0 ms: 1.10x faster                                                      |
| regex_dna                | 136 ms                                                      | 125 ms: 1.09x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 52.5 ms: 1.09x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.02 us: 1.09x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                                     |
| 2to3                     | 246 ms                                                      | 232 ms: 1.06x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.6 ms: 1.06x faster                                                      |
| sympy_str                | 194 ms                                                      | 184 ms: 1.06x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 42.5 ms: 1.05x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.18 sec: 1.04x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 573 ms: 1.03x faster                                                       |
| json                     | 3.14 ms                                                     | 3.07 ms: 1.02x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 202 ms: 1.02x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.01x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 95.6 ms: 1.01x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.66 sec: 1.01x faster                                                     |
| sympy_expand             | 314 ms                                                      | 312 ms: 1.01x faster                                                       |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.02x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.2 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.78 ms: 1.02x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.94 us: 1.03x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 78.0 ms: 1.03x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.48 us: 1.04x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 59.1 ms: 1.06x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 81.0 ms: 1.07x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 16.7 ms: 1.08x slower                                                      |
| scimark_fft              | 187 ms                                                      | 205 ms: 1.09x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.11x slower                                                      |
| async_generators         | 222 ms                                                      | 249 ms: 1.12x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 69.9 ms: 1.13x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 913 us: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                      |
| fannkuch                 | 256 ms                                                      | 298 ms: 1.17x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.6 ms: 1.22x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.97 ms: 1.26x slower                                                      |
| nbody                    | 71.3 ms                                                     | 91.2 ms: 1.28x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (3): pycparser, spectral_norm, nqueens
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240802-3.14.0a0-498376d/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown