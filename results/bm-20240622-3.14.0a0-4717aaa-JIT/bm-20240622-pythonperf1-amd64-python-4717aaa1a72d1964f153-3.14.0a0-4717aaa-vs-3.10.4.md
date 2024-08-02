# Results vs. 3.10.4

- fork: python
- ref: 4717aaa1a72d1964f153
- machine: windows-amd64
- commit hash: 4717aaa
- commit date: 2024-06-22
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                     |
| html5lib       | 51.0 ms                                                     | 35.7 ms: 1.43x faster                                                      |
| tornado_http   | 108 ms                                                      | 82.7 ms: 1.31x faster                                                      |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 495 ms: 2.24x faster                                                       |
| async_tree_none         | 435 ms                                                      | 198 ms: 2.20x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 242 ms: 2.17x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 377 ms: 1.69x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.06x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                      |
| nbody          | 71.3 ms                                                     | 53.6 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.2 ms: 1.22x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 17.2 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.65 ms: 1.62x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 168 us: 1.60x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 123 us: 1.49x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.21 sec: 1.39x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.3 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.6 ms: 1.05x faster                                                      |
| unpickle             | 9.09 us                                                     | 9.00 us: 1.01x faster                                                      |
| pickle_dict          | 17.2 us                                                     | 17.7 us: 1.03x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.80 us: 1.03x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.86 us: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.29 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.5 ms: 1.09x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.08 ms: 1.78x faster                                                      |
| django_template | 28.9 ms                                                     | 24.6 ms: 1.18x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.2 ms: 1.15x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 41.8 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.05x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 495 ms: 2.24x faster                                                       |
| async_tree_none          | 435 ms                                                      | 198 ms: 2.20x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 242 ms: 2.17x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.09 ms: 2.00x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 15.3 us: 1.88x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.08 ms: 1.78x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 55.4 ns: 1.71x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 377 ms: 1.69x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 46.3 ms: 1.67x faster                                                      |
| raytrace                 | 273 ms                                                      | 168 ms: 1.63x faster                                                       |
| pyflate                  | 409 ms                                                      | 252 ms: 1.62x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.65 ms: 1.62x faster                                                      |
| generators               | 32.4 ms                                                     | 20.0 ms: 1.62x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.61x faster                                                      |
| chaos                    | 61.7 ms                                                     | 38.5 ms: 1.60x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 168 us: 1.60x faster                                                       |
| go                       | 139 ms                                                      | 88.0 ms: 1.58x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 775 us: 1.57x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.8 ms: 1.54x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 40.7 ms: 1.54x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 477 ms: 1.53x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.4 ms: 1.53x faster                                                      |
| pylint                   | 350 ms                                                      | 232 ms: 1.51x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 123 us: 1.49x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.01 ms: 1.47x faster                                                      |
| deepcopy                 | 255 us                                                      | 175 us: 1.46x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.48 sec: 1.43x faster                                                     |
| html5lib                 | 51.0 ms                                                     | 35.7 ms: 1.43x faster                                                      |
| richards                 | 42.4 ms                                                     | 30.2 ms: 1.41x faster                                                      |
| float                    | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.21 sec: 1.39x faster                                                     |
| scimark_sor              | 106 ms                                                      | 79.3 ms: 1.34x faster                                                      |
| nbody                    | 71.3 ms                                                     | 53.6 ms: 1.33x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 924 ms: 1.32x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 450 ms: 1.32x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.68 us: 1.31x faster                                                      |
| tornado_http             | 108 ms                                                      | 82.7 ms: 1.31x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.09 ms: 1.30x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.37 sec: 1.30x faster                                                     |
| scimark_fft              | 187 ms                                                      | 150 ms: 1.25x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 68.8 ms: 1.25x faster                                                      |
| coroutines               | 16.0 ms                                                     | 12.8 ms: 1.25x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 768 us: 1.25x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.62 ms: 1.24x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                      |
| regex_compile            | 106 ms                                                      | 87.2 ms: 1.22x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                      |
| thrift                   | 617 us                                                      | 510 us: 1.21x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.5 ms: 1.18x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.6 ms: 1.18x faster                                                      |
| pycparser                | 930 ms                                                      | 796 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| fannkuch                 | 256 ms                                                      | 222 ms: 1.15x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.2 ms: 1.15x faster                                                      |
| logging_format           | 6.76 us                                                     | 5.87 us: 1.15x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.49 us: 1.13x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.12x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 59.5 ms: 1.12x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 35.6 ms: 1.12x faster                                                      |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                     |
| sqlglot_normalize        | 205 ms                                                      | 188 ms: 1.09x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.3 ms: 1.08x faster                                                      |
| 2to3                     | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.6 ms: 1.05x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.6 ms: 1.05x faster                                                      |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                                       |
| unpickle                 | 9.09 us                                                     | 9.00 us: 1.01x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 41.8 ms: 1.02x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 17.7 us: 1.03x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.80 us: 1.03x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.86 us: 1.04x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.29 us: 1.07x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.5 ms: 1.09x slower                                                      |
| async_generators         | 222 ms                                                      | 243 ms: 1.10x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 17.2 ms: 1.11x slower                                                      |
| coverage                 | 39.0 ms                                                     | 43.6 ms: 1.12x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 69.9 ms: 1.13x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.48 ms: 1.14x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 914 us: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (3): pidigits, json_loads, pathlib
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240622-3.14.0a0-4717aaa-JIT/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown