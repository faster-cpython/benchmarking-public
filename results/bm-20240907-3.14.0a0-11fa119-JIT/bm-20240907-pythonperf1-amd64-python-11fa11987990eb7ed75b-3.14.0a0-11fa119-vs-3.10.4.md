# Results vs. 3.10.4

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-amd64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 241 ms: 1.02x faster                                                       |
| html5lib       | 51.0 ms                                                     | 42.0 ms: 1.22x faster                                                      |
| tornado_http   | 108 ms                                                      | 97.7 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 201 ms: 2.17x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 258 ms: 2.04x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 584 ms: 1.90x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 393 ms: 1.62x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 49.0 ms: 1.46x faster                                                      |
| float          | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.27x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 95.2 ms: 1.11x faster                                                      |
| regex_dna      | 136 ms                                                      | 124 ms: 1.10x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 15.2 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.86 ms: 1.56x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 194 us: 1.39x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.24 sec: 1.34x faster                                                     |
| unpickle_pure_python | 183 us                                                      | 141 us: 1.30x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 34.7 ms: 1.28x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 49.0 ms: 1.13x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.6 ms: 1.05x faster                                                      |
| unpickle             | 9.09 us                                                     | 9.18 us: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 17.7 us: 1.03x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.80 us: 1.03x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.87 us: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.17 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.5 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.15 ms: 1.75x faster                                                      |
| django_template | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 44.0 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 108 us: 3.10x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.83 ms: 2.28x faster                                                      |
| async_tree_none          | 435 ms                                                      | 201 ms: 2.17x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 258 ms: 2.04x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 584 ms: 1.90x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 15.2 us: 1.90x faster                                                      |
| scimark_sor              | 106 ms                                                      | 59.9 ms: 1.77x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.15 ms: 1.75x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 45.6 ms: 1.69x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 57.3 ns: 1.65x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 52.3 ms: 1.64x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 38.3 ms: 1.63x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 393 ms: 1.62x faster                                                       |
| pyflate                  | 409 ms                                                      | 261 ms: 1.57x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.86 ms: 1.56x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.56x faster                                                      |
| go                       | 139 ms                                                      | 91.4 ms: 1.52x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.6 ms: 1.52x faster                                                      |
| nbody                    | 71.3 ms                                                     | 49.0 ms: 1.46x faster                                                      |
| generators               | 32.4 ms                                                     | 22.8 ms: 1.42x faster                                                      |
| float                    | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 523 ms: 1.40x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 194 us: 1.39x faster                                                       |
| raytrace                 | 273 ms                                                      | 196 ms: 1.39x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 883 us: 1.38x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.1 ms: 1.36x faster                                                      |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                       |
| richards_super           | 52.2 ms                                                     | 38.4 ms: 1.36x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.24 sec: 1.34x faster                                                     |
| pycparser                | 930 ms                                                      | 706 ms: 1.32x faster                                                       |
| pylint                   | 350 ms                                                      | 266 ms: 1.32x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.62 sec: 1.30x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 141 us: 1.30x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.15 ms: 1.28x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 34.7 ms: 1.28x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.12 ms: 1.28x faster                                                      |
| scimark_fft              | 187 ms                                                      | 148 ms: 1.27x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.22x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 42.0 ms: 1.22x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.19x faster                                                     |
| thrift                   | 617 us                                                      | 520 us: 1.19x faster                                                       |
| richards                 | 42.4 ms                                                     | 35.8 ms: 1.18x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.03 sec: 1.18x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 503 ms: 1.18x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.0 ms: 1.17x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.92 ms: 1.17x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 822 us: 1.16x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 49.0 ms: 1.13x faster                                                      |
| regex_compile            | 106 ms                                                      | 95.2 ms: 1.11x faster                                                      |
| tornado_http             | 108 ms                                                      | 97.7 ms: 1.11x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                      |
| fannkuch                 | 256 ms                                                      | 232 ms: 1.10x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 60.5 ms: 1.10x faster                                                      |
| regex_dna                | 136 ms                                                      | 124 ms: 1.10x faster                                                       |
| sympy_sum                | 107 ms                                                      | 97.8 ms: 1.09x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| json                     | 3.14 ms                                                     | 2.97 ms: 1.06x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.43 us: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.6 ms: 1.05x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.97 us: 1.04x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.8 ms: 1.04x faster                                                      |
| sympy_str                | 194 ms                                                      | 188 ms: 1.03x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 200 ms: 1.03x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                      |
| 2to3                     | 246 ms                                                      | 241 ms: 1.02x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.2 ms: 1.02x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 75.1 ms: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| unpickle                 | 9.09 us                                                     | 9.18 us: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 17.7 us: 1.03x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.80 us: 1.03x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.87 us: 1.04x slower                                                      |
| sympy_expand             | 314 ms                                                      | 329 ms: 1.05x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.17 us: 1.05x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 79.5 ms: 1.05x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 44.0 ms: 1.07x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 914 us: 1.14x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 71.6 ms: 1.15x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.64 ms: 1.18x slower                                                      |
| async_generators         | 222 ms                                                      | 264 ms: 1.19x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.5 ms: 1.19x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.2 ms: 1.24x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 58.4 ns: 1.47x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                               |

Benchmark hidden because not significant (2): docutils, sqlglot_optimize
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown