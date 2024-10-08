# Results vs. 3.10.4

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-amd64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.9 ms: 1.28x faster                                                      |
| tornado_http   | 108 ms                                                      | 93.8 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 260 ms: 2.03x faster                                                       |
| async_tree_none         | 435 ms                                                      | 217 ms: 2.01x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 613 ms: 1.81x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 383 ms: 1.66x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 57.2 ms: 1.08x faster                                                      |
| pidigits       | 149 ms                                                      | 152 ms: 1.02x slower                                                       |
| nbody          | 71.3 ms                                                     | 84.6 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.8 ms: 1.17x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 15.1 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.21 ms: 1.48x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 213 us: 1.27x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 150 us: 1.22x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 94.3 ms: 1.03x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.78 us: 1.02x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 58.4 ms: 1.05x slower                                                      |
| unpickle             | 9.09 us                                                     | 9.64 us: 1.06x slower                                                      |
| pickle               | 6.85 us                                                     | 7.44 us: 1.09x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.99 us: 1.09x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.0 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.85 ms: 1.32x faster                                                      |
| django_template | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.97x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 260 ms: 2.03x faster                                                       |
| async_tree_none          | 435 ms                                                      | 217 ms: 2.01x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 613 ms: 1.81x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 383 ms: 1.66x faster                                                       |
| go                       | 139 ms                                                      | 86.9 ms: 1.60x faster                                                      |
| pylint                   | 350 ms                                                      | 226 ms: 1.55x faster                                                       |
| generators               | 32.4 ms                                                     | 20.9 ms: 1.55x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 62.5 ns: 1.51x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.21 ms: 1.48x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.1 ms: 1.45x faster                                                      |
| chaos                    | 61.7 ms                                                     | 43.0 ms: 1.43x faster                                                      |
| raytrace                 | 273 ms                                                      | 191 ms: 1.43x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.3 us: 1.42x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 525 ms: 1.39x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 892 us: 1.36x faster                                                       |
| deepcopy                 | 255 us                                                      | 189 us: 1.35x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.59 sec: 1.33x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 64.7 ms: 1.33x faster                                                      |
| richards                 | 42.4 ms                                                     | 32.1 ms: 1.32x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.85 ms: 1.32x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.8 ms: 1.31x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 39.9 ms: 1.28x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.50 ms: 1.28x faster                                                      |
| pyflate                  | 409 ms                                                      | 321 ms: 1.28x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 213 us: 1.27x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 150 us: 1.22x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                     |
| pycparser                | 930 ms                                                      | 767 ms: 1.21x faster                                                       |
| thrift                   | 617 us                                                      | 515 us: 1.20x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                      |
| sympy_sum                | 107 ms                                                      | 91.1 ms: 1.17x faster                                                      |
| regex_compile            | 106 ms                                                      | 90.8 ms: 1.17x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.1 ms: 1.17x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 823 us: 1.16x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.16x faster                                                      |
| scimark_sor              | 106 ms                                                      | 91.5 ms: 1.16x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                      |
| tornado_http             | 108 ms                                                      | 93.8 ms: 1.16x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 44.1 ms: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.4 ms: 1.14x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 69.0 ms: 1.12x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.2 ms: 1.10x faster                                                      |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                     |
| sqlglot_normalize        | 205 ms                                                      | 190 ms: 1.08x faster                                                       |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                      |
| float                    | 61.7 ms                                                     | 57.2 ms: 1.08x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 549 ms: 1.08x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 63.8 ms: 1.04x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| xml_etree_parse          | 96.8 ms                                                     | 94.3 ms: 1.03x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 15.1 ms: 1.02x faster                                                      |
| sympy_expand             | 314 ms                                                      | 307 ms: 1.02x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.64 us: 1.02x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 40.3 ns: 1.02x slower                                                      |
| pidigits                 | 149 ms                                                      | 152 ms: 1.02x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.78 us: 1.02x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.79 ms: 1.02x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 79.0 ms: 1.04x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 79.4 ms: 1.05x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 58.4 ms: 1.05x slower                                                      |
| unpickle                 | 9.09 us                                                     | 9.64 us: 1.06x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.44 us: 1.09x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.99 us: 1.09x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 67.8 ms: 1.09x slower                                                      |
| scimark_fft              | 187 ms                                                      | 205 ms: 1.10x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.0 us: 1.10x slower                                                      |
| async_generators         | 222 ms                                                      | 249 ms: 1.12x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 902 us: 1.13x slower                                                       |
| fannkuch                 | 256 ms                                                      | 291 ms: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                      |
| nbody                    | 71.3 ms                                                     | 84.6 ms: 1.19x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.6 ms: 1.25x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.12 ms: 1.30x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (3): logging_simple, xml_etree_iterparse, json
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown