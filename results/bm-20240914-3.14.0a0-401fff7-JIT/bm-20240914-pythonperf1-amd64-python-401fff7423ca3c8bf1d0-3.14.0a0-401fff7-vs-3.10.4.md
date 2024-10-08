# Results vs. 3.10.4

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-amd64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 239 ms: 1.03x faster                                                       |
| html5lib       | 51.0 ms                                                     | 42.1 ms: 1.21x faster                                                      |
| tornado_http   | 108 ms                                                      | 87.4 ms: 1.24x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 206 ms: 2.11x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 258 ms: 2.04x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 583 ms: 1.90x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.91x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 49.4 ms: 1.44x faster                                                      |
| float          | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                      |
| Geometric mean | (ref)                                                       | 1.26x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| regex_compile  | 106 ms                                                      | 94.2 ms: 1.13x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.9 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.73 ms: 1.60x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 196 us: 1.37x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.26 sec: 1.33x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 34.8 ms: 1.28x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 145 us: 1.26x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 49.0 ms: 1.13x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.7 ms: 1.07x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.4 ms: 1.05x faster                                                      |
| unpickle             | 9.09 us                                                     | 9.27 us: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 17.9 us: 1.04x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.87 us: 1.06x slower                                                      |
| pickle               | 6.85 us                                                     | 7.38 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.6 ms: 1.05x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.26 ms: 1.72x faster                                                      |
| django_template | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.9 ms: 1.05x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 45.7 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.04x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.82 ms: 2.30x faster                                                      |
| async_tree_none          | 435 ms                                                      | 206 ms: 2.11x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 258 ms: 2.04x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 14.8 us: 1.94x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 583 ms: 1.90x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 43.3 ms: 1.78x faster                                                      |
| scimark_sor              | 106 ms                                                      | 60.7 ms: 1.75x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.26 ms: 1.72x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 57.2 ns: 1.66x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 38.6 ms: 1.62x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.73 ms: 1.60x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 463 ms: 1.58x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 54.4 ms: 1.58x faster                                                      |
| pyflate                  | 409 ms                                                      | 265 ms: 1.55x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.55x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.0 ms: 1.54x faster                                                      |
| generators               | 32.4 ms                                                     | 21.1 ms: 1.53x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.39 sec: 1.52x faster                                                     |
| go                       | 139 ms                                                      | 92.2 ms: 1.51x faster                                                      |
| nbody                    | 71.3 ms                                                     | 49.4 ms: 1.44x faster                                                      |
| deepcopy                 | 255 us                                                      | 181 us: 1.41x faster                                                       |
| float                    | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 196 us: 1.37x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 886 us: 1.37x faster                                                       |
| raytrace                 | 273 ms                                                      | 202 ms: 1.35x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.7 ms: 1.34x faster                                                      |
| richards_super           | 52.2 ms                                                     | 39.1 ms: 1.33x faster                                                      |
| pylint                   | 350 ms                                                      | 263 ms: 1.33x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.26 sec: 1.33x faster                                                     |
| pycparser                | 930 ms                                                      | 715 ms: 1.30x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.14 ms: 1.29x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.13 ms: 1.28x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 34.8 ms: 1.28x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 145 us: 1.26x faster                                                       |
| scimark_fft              | 187 ms                                                      | 149 ms: 1.26x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.43 sec: 1.24x faster                                                     |
| tornado_http             | 108 ms                                                      | 87.4 ms: 1.24x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.79 us: 1.23x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 42.1 ms: 1.21x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.20x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.3 ms: 1.19x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 809 us: 1.18x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.03 sec: 1.18x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 503 ms: 1.18x faster                                                       |
| thrift                   | 617 us                                                      | 525 us: 1.18x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.89 ms: 1.17x faster                                                      |
| richards                 | 42.4 ms                                                     | 36.5 ms: 1.16x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 49.0 ms: 1.13x faster                                                      |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| regex_compile            | 106 ms                                                      | 94.2 ms: 1.13x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 59.6 ms: 1.12x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                      |
| sympy_sum                | 107 ms                                                      | 97.9 ms: 1.09x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.7 ms: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.95 ms: 1.06x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.4 ms: 1.05x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.45 us: 1.05x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.9 ms: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.9 ms: 1.03x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 199 ms: 1.03x faster                                                       |
| fannkuch                 | 256 ms                                                      | 248 ms: 1.03x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.8 ms: 1.03x faster                                                      |
| sympy_str                | 194 ms                                                      | 189 ms: 1.03x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.06 us: 1.03x faster                                                      |
| 2to3                     | 246 ms                                                      | 239 ms: 1.03x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 74.9 ms: 1.01x faster                                                      |
| pathlib                  | 75.7 ms                                                     | 74.8 ms: 1.01x faster                                                      |
| unpickle                 | 9.09 us                                                     | 9.27 us: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 17.9 us: 1.04x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.6 ms: 1.05x slower                                                      |
| sympy_expand             | 314 ms                                                      | 330 ms: 1.05x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.87 us: 1.06x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.38 us: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 45.7 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 901 us: 1.13x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 71.7 ms: 1.16x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.60 ms: 1.17x slower                                                      |
| async_generators         | 222 ms                                                      | 260 ms: 1.17x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.1 ms: 1.23x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 56.9 ns: 1.44x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                               |

Benchmark hidden because not significant (4): docutils, sqlglot_optimize, pidigits, pickle_list
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown