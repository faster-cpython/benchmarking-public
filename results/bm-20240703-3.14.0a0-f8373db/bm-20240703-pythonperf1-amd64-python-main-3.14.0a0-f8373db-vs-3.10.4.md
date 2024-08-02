# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: f8373db
- commit date: 2024-07-03
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 216 ms: 1.14x faster                                       |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                     |
| html5lib       | 51.0 ms                                                     | 36.8 ms: 1.39x faster                                      |
| tornado_http   | 108 ms                                                      | 80.2 ms: 1.35x faster                                      |
| Geometric mean | (ref)                                                       | 1.26x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 204 ms: 2.13x faster                                       |
| async_tree_io           | 1.11 sec                                                    | 523 ms: 2.12x faster                                       |
| async_tree_memoization  | 526 ms                                                      | 249 ms: 2.11x faster                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 381 ms: 1.67x faster                                       |
| Geometric mean          | (ref)                                                       | 2.00x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 61.7 ms                                                     | 54.0 ms: 1.14x faster                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                       |
| nbody          | 71.3 ms                                                     | 73.6 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.2 ms: 1.32x faster                                      |
| regex_dna      | 136 ms                                                      | 125 ms: 1.09x faster                                       |
| regex_v8       | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                      |
| regex_effbot   | 1.66 ms                                                     | 1.64 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.80 ms: 1.58x faster                                      |
| pickle_pure_python   | 270 us                                                      | 189 us: 1.43x faster                                       |
| unpickle_pure_python | 183 us                                                      | 135 us: 1.36x faster                                       |
| xml_etree_process    | 44.5 ms                                                     | 38.4 ms: 1.16x faster                                      |
| tomli_loads          | 1.67 sec                                                    | 1.48 sec: 1.13x faster                                     |
| xml_etree_parse      | 96.8 ms                                                     | 93.1 ms: 1.04x faster                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                      |
| Geometric mean       | (ref)                                                       | 1.17x faster                                               |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.9 ms: 1.01x slower                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                      |
| Geometric mean         | (ref)                                                       | 1.06x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.82 ms: 1.33x faster                                      |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                      |
| django_template | 28.9 ms                                                     | 22.7 ms: 1.28x faster                                      |
| genshi_xml      | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                      |
| Geometric mean  | (ref)                                                       | 1.27x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.22x faster                                       |
| async_tree_none          | 435 ms                                                      | 204 ms: 2.13x faster                                       |
| async_tree_io            | 1.11 sec                                                    | 523 ms: 2.12x faster                                       |
| async_tree_memoization   | 526 ms                                                      | 249 ms: 2.11x faster                                       |
| deltablue                | 4.19 ms                                                     | 2.03 ms: 2.06x faster                                      |
| richards_super           | 52.2 ms                                                     | 30.9 ms: 1.69x faster                                      |
| pylint                   | 350 ms                                                      | 208 ms: 1.68x faster                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 381 ms: 1.67x faster                                       |
| raytrace                 | 273 ms                                                      | 170 ms: 1.61x faster                                       |
| go                       | 139 ms                                                      | 86.4 ms: 1.61x faster                                      |
| json_dumps               | 9.16 ms                                                     | 5.80 ms: 1.58x faster                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.5 us: 1.56x faster                                      |
| generators               | 32.4 ms                                                     | 20.8 ms: 1.56x faster                                      |
| asyncio_tcp              | 732 ms                                                      | 471 ms: 1.55x faster                                       |
| logging_silent           | 94.6 ns                                                     | 60.9 ns: 1.55x faster                                      |
| richards                 | 42.4 ms                                                     | 27.3 ms: 1.55x faster                                      |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                      |
| scimark_lu               | 85.8 ms                                                     | 56.8 ms: 1.51x faster                                      |
| chaos                    | 61.7 ms                                                     | 41.3 ms: 1.49x faster                                      |
| sqlglot_parse            | 1.22 ms                                                     | 820 us: 1.48x faster                                       |
| deepcopy                 | 255 us                                                      | 172 us: 1.48x faster                                       |
| hexiom                   | 5.74 ms                                                     | 3.92 ms: 1.46x faster                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.03 ms: 1.43x faster                                      |
| pickle_pure_python       | 270 us                                                      | 189 us: 1.43x faster                                       |
| html5lib                 | 51.0 ms                                                     | 36.8 ms: 1.39x faster                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.53 sec: 1.38x faster                                     |
| pyflate                  | 409 ms                                                      | 298 ms: 1.37x faster                                       |
| unpickle_pure_python     | 183 us                                                      | 135 us: 1.36x faster                                       |
| tornado_http             | 108 ms                                                      | 80.2 ms: 1.35x faster                                      |
| mako                     | 9.03 ms                                                     | 6.82 ms: 1.33x faster                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.2 ms: 1.32x faster                                      |
| regex_compile            | 106 ms                                                      | 80.2 ms: 1.32x faster                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.4 ms: 1.32x faster                                      |
| scimark_sor              | 106 ms                                                      | 80.4 ms: 1.32x faster                                      |
| pycparser                | 930 ms                                                      | 705 ms: 1.32x faster                                       |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                      |
| django_template          | 28.9 ms                                                     | 22.7 ms: 1.28x faster                                      |
| sympy_sum                | 107 ms                                                      | 85.1 ms: 1.26x faster                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.77 us: 1.25x faster                                      |
| bench_thread_pool        | 958 us                                                      | 772 us: 1.24x faster                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.22x faster                                      |
| thrift                   | 617 us                                                      | 509 us: 1.21x faster                                       |
| genshi_xml               | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                      |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.20x faster                                     |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.20x faster                                      |
| sympy_str                | 194 ms                                                      | 163 ms: 1.19x faster                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 33.4 ms: 1.19x faster                                      |
| spectral_norm            | 77.3 ms                                                     | 64.9 ms: 1.19x faster                                      |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                     |
| pprint_pformat           | 1.22 sec                                                    | 1.04 sec: 1.17x faster                                     |
| pprint_safe_repr         | 592 ms                                                      | 509 ms: 1.16x faster                                       |
| sqlglot_normalize        | 205 ms                                                      | 177 ms: 1.16x faster                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.4 ms: 1.16x faster                                      |
| float                    | 61.7 ms                                                     | 54.0 ms: 1.14x faster                                      |
| 2to3                     | 246 ms                                                      | 216 ms: 1.14x faster                                       |
| nqueens                  | 66.6 ms                                                     | 58.4 ms: 1.14x faster                                      |
| tomli_loads              | 1.67 sec                                                    | 1.48 sec: 1.13x faster                                     |
| sympy_expand             | 314 ms                                                      | 278 ms: 1.13x faster                                       |
| regex_dna                | 136 ms                                                      | 125 ms: 1.09x faster                                       |
| logging_format           | 6.76 us                                                     | 6.35 us: 1.06x faster                                      |
| logging_simple           | 6.22 us                                                     | 5.89 us: 1.06x faster                                      |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.1 ms: 1.04x faster                                      |
| meteor_contest           | 75.9 ms                                                     | 73.3 ms: 1.04x faster                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.63 ms: 1.04x faster                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                      |
| regex_v8                 | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                      |
| regex_effbot             | 1.66 ms                                                     | 1.64 ms: 1.01x faster                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                       |
| scimark_fft              | 187 ms                                                      | 189 ms: 1.01x slower                                       |
| python_startup           | 20.6 ms                                                     | 20.9 ms: 1.01x slower                                      |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                      |
| nbody                    | 71.3 ms                                                     | 73.6 ms: 1.03x slower                                      |
| async_generators         | 222 ms                                                      | 232 ms: 1.05x slower                                       |
| bench_mp_pool            | 62.0 ms                                                     | 65.2 ms: 1.05x slower                                      |
| fannkuch                 | 256 ms                                                      | 276 ms: 1.08x slower                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                      |
| create_gc_cycles         | 800 us                                                      | 903 us: 1.13x slower                                       |
| coverage                 | 39.0 ms                                                     | 45.2 ms: 1.16x slower                                      |
| telco                    | 3.94 ms                                                     | 4.75 ms: 1.21x slower                                      |
| Geometric mean           | (ref)                                                       | 1.26x faster                                               |

Benchmark hidden because not significant (2): pathlib, xml_etree_generate
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240703-3.14.0a0-f8373db/bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown