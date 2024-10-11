# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: dd0ee20
- commit date: 2024-10-10
- overall geometric mean: 1.02x faster
- HPT reliability: 88.63%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 283 ms: 1.15x slower                                       |
| docutils       | 1.92 sec                                                    | 2.17 sec: 1.13x slower                                     |
| html5lib       | 51.0 ms                                                     | 46.3 ms: 1.10x faster                                      |
| tornado_http   | 108 ms                                                      | 106 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 238 ms: 1.83x faster                                       |
| async_tree_memoization  | 526 ms                                                      | 298 ms: 1.77x faster                                       |
| async_tree_io           | 1.11 sec                                                    | 639 ms: 1.74x faster                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 446 ms: 1.43x faster                                       |
| Geometric mean          | (ref)                                                       | 1.68x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 48.1 ms: 1.48x faster                                      |
| float          | 61.7 ms                                                     | 54.6 ms: 1.13x faster                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 115 ms: 1.19x faster                                       |
| regex_compile  | 106 ms                                                      | 107 ms: 1.01x slower                                       |
| regex_v8       | 15.4 ms                                                     | 16.7 ms: 1.08x slower                                      |
| regex_effbot   | 1.66 ms                                                     | 1.85 ms: 1.12x slower                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 7.69 ms: 1.19x faster                                      |
| tomli_loads          | 1.67 sec                                                    | 1.47 sec: 1.14x faster                                     |
| pickle_pure_python   | 270 us                                                      | 251 us: 1.07x faster                                       |
| xml_etree_process    | 44.5 ms                                                     | 46.7 ms: 1.05x slower                                      |
| xml_etree_parse      | 96.8 ms                                                     | 109 ms: 1.13x slower                                       |
| unpickle_pure_python | 183 us                                                      | 207 us: 1.13x slower                                       |
| unpickle_list        | 2.71 us                                                     | 3.07 us: 1.13x slower                                      |
| xml_etree_generate   | 55.5 ms                                                     | 64.6 ms: 1.16x slower                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 76.0 ms: 1.17x slower                                      |
| pickle               | 6.85 us                                                     | 8.55 us: 1.25x slower                                      |
| unpickle             | 9.09 us                                                     | 11.4 us: 1.25x slower                                      |
| pickle_list          | 2.75 us                                                     | 3.56 us: 1.29x slower                                      |
| pickle_dict          | 17.2 us                                                     | 22.9 us: 1.33x slower                                      |
| json_loads           | 14.0 us                                                     | 21.2 us: 1.51x slower                                      |
| Geometric mean       | (ref)                                                       | 1.13x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.2 ms: 1.17x slower                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.9 ms: 1.29x slower                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.17 ms: 1.46x faster                                      |
| genshi_text     | 19.8 ms                                                     | 21.4 ms: 1.08x slower                                      |
| django_template | 28.9 ms                                                     | 32.7 ms: 1.13x slower                                      |
| genshi_xml      | 41.0 ms                                                     | 50.1 ms: 1.22x slower                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 132 us: 2.55x faster                                       |
| deltablue                | 4.19 ms                                                     | 2.27 ms: 1.84x faster                                      |
| async_tree_none          | 435 ms                                                      | 238 ms: 1.83x faster                                       |
| async_tree_memoization   | 526 ms                                                      | 298 ms: 1.77x faster                                       |
| async_tree_io            | 1.11 sec                                                    | 639 ms: 1.74x faster                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.6 us: 1.55x faster                                      |
| nbody                    | 71.3 ms                                                     | 48.1 ms: 1.48x faster                                      |
| mako                     | 9.03 ms                                                     | 6.17 ms: 1.46x faster                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 446 ms: 1.43x faster                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.57 sec: 1.35x faster                                     |
| logging_silent           | 94.6 ns                                                     | 71.4 ns: 1.32x faster                                      |
| pyflate                  | 409 ms                                                      | 309 ms: 1.32x faster                                       |
| scimark_sor              | 106 ms                                                      | 80.7 ms: 1.32x faster                                      |
| spectral_norm            | 77.3 ms                                                     | 58.8 ms: 1.31x faster                                      |
| asyncio_tcp              | 732 ms                                                      | 563 ms: 1.30x faster                                       |
| chaos                    | 61.7 ms                                                     | 47.7 ms: 1.29x faster                                      |
| comprehensions           | 16.5 us                                                     | 12.8 us: 1.29x faster                                      |
| crypto_pyaes             | 62.5 ms                                                     | 49.0 ms: 1.28x faster                                      |
| generators               | 32.4 ms                                                     | 26.0 ms: 1.25x faster                                      |
| go                       | 139 ms                                                      | 112 ms: 1.24x faster                                       |
| deepcopy                 | 255 us                                                      | 214 us: 1.20x faster                                       |
| json_dumps               | 9.16 ms                                                     | 7.69 ms: 1.19x faster                                      |
| regex_dna                | 136 ms                                                      | 115 ms: 1.19x faster                                       |
| richards_super           | 52.2 ms                                                     | 44.4 ms: 1.18x faster                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.0 ms: 1.17x faster                                      |
| sqlglot_parse            | 1.22 ms                                                     | 1.04 ms: 1.17x faster                                      |
| pylint                   | 350 ms                                                      | 302 ms: 1.16x faster                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                     |
| tomli_loads              | 1.67 sec                                                    | 1.47 sec: 1.14x faster                                     |
| pprint_safe_repr         | 592 ms                                                      | 523 ms: 1.13x faster                                       |
| float                    | 61.7 ms                                                     | 54.6 ms: 1.13x faster                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.43 ms: 1.12x faster                                      |
| pycparser                | 930 ms                                                      | 833 ms: 1.12x faster                                       |
| raytrace                 | 273 ms                                                      | 245 ms: 1.12x faster                                       |
| html5lib                 | 51.0 ms                                                     | 46.3 ms: 1.10x faster                                      |
| sqlite_synth             | 1.91 us                                                     | 1.75 us: 1.09x faster                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.35 ms: 1.09x faster                                      |
| pickle_pure_python       | 270 us                                                      | 251 us: 1.07x faster                                       |
| mdp                      | 1.78 sec                                                    | 1.67 sec: 1.06x faster                                     |
| dulwich_log              | 50.5 ms                                                     | 47.6 ms: 1.06x faster                                      |
| scimark_fft              | 187 ms                                                      | 179 ms: 1.05x faster                                       |
| scimark_lu               | 85.8 ms                                                     | 82.8 ms: 1.04x faster                                      |
| richards                 | 42.4 ms                                                     | 41.0 ms: 1.03x faster                                      |
| tornado_http             | 108 ms                                                      | 106 ms: 1.02x faster                                       |
| regex_compile            | 106 ms                                                      | 107 ms: 1.01x slower                                       |
| hexiom                   | 5.74 ms                                                     | 5.85 ms: 1.02x slower                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.27 us: 1.03x slower                                      |
| xml_etree_process        | 44.5 ms                                                     | 46.7 ms: 1.05x slower                                      |
| meteor_contest           | 75.9 ms                                                     | 80.0 ms: 1.05x slower                                      |
| thrift                   | 617 us                                                      | 656 us: 1.06x slower                                       |
| fannkuch                 | 256 ms                                                      | 274 ms: 1.07x slower                                       |
| regex_v8                 | 15.4 ms                                                     | 16.7 ms: 1.08x slower                                      |
| genshi_text              | 19.8 ms                                                     | 21.4 ms: 1.08x slower                                      |
| pathlib                  | 75.7 ms                                                     | 82.0 ms: 1.08x slower                                      |
| sympy_sum                | 107 ms                                                      | 118 ms: 1.10x slower                                       |
| regex_effbot             | 1.66 ms                                                     | 1.85 ms: 1.12x slower                                      |
| xml_etree_parse          | 96.8 ms                                                     | 109 ms: 1.13x slower                                       |
| unpickle_pure_python     | 183 us                                                      | 207 us: 1.13x slower                                       |
| nqueens                  | 66.6 ms                                                     | 75.2 ms: 1.13x slower                                      |
| logging_format           | 6.76 us                                                     | 7.64 us: 1.13x slower                                      |
| unpickle_list            | 2.71 us                                                     | 3.07 us: 1.13x slower                                      |
| docutils                 | 1.92 sec                                                    | 2.17 sec: 1.13x slower                                     |
| django_template          | 28.9 ms                                                     | 32.7 ms: 1.13x slower                                      |
| sympy_integrate          | 15.3 ms                                                     | 17.3 ms: 1.13x slower                                      |
| logging_simple           | 6.22 us                                                     | 7.14 us: 1.15x slower                                      |
| 2to3                     | 246 ms                                                      | 283 ms: 1.15x slower                                       |
| sympy_str                | 194 ms                                                      | 226 ms: 1.16x slower                                       |
| xml_etree_generate       | 55.5 ms                                                     | 64.6 ms: 1.16x slower                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 76.0 ms: 1.17x slower                                      |
| python_startup           | 20.6 ms                                                     | 24.2 ms: 1.17x slower                                      |
| sqlglot_normalize        | 205 ms                                                      | 244 ms: 1.19x slower                                       |
| json                     | 3.14 ms                                                     | 3.78 ms: 1.21x slower                                      |
| genshi_xml               | 41.0 ms                                                     | 50.1 ms: 1.22x slower                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 49.1 ms: 1.23x slower                                      |
| sympy_expand             | 314 ms                                                      | 389 ms: 1.24x slower                                       |
| coroutines               | 16.0 ms                                                     | 19.9 ms: 1.24x slower                                      |
| pickle                   | 6.85 us                                                     | 8.55 us: 1.25x slower                                      |
| unpickle                 | 9.09 us                                                     | 11.4 us: 1.25x slower                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.9 ms: 1.29x slower                                      |
| pickle_list              | 2.75 us                                                     | 3.56 us: 1.29x slower                                      |
| pickle_dict              | 17.2 us                                                     | 22.9 us: 1.33x slower                                      |
| telco                    | 3.94 ms                                                     | 5.30 ms: 1.35x slower                                      |
| bench_mp_pool            | 62.0 ms                                                     | 83.6 ms: 1.35x slower                                      |
| create_gc_cycles         | 800 us                                                      | 1.08 ms: 1.35x slower                                      |
| unpack_sequence          | 39.6 ns                                                     | 58.7 ns: 1.48x slower                                      |
| json_loads               | 14.0 us                                                     | 21.2 us: 1.51x slower                                      |
| coverage                 | 39.0 ms                                                     | 59.6 ms: 1.53x slower                                      |
| async_generators         | 222 ms                                                      | 351 ms: 1.58x slower                                       |
| gc_traversal             | 1.41 ms                                                     | 2.52 ms: 1.79x slower                                      |
| Geometric mean           | (ref)                                                       | 1.02x faster                                               |

Benchmark hidden because not significant (2): bench_thread_pool, pidigits
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241010-3.14.0a0-dd0ee20-JIT/bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 88.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown